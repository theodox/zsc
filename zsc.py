#zsc.py

import io
import ast
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


WARN_ON_COMPARISONS = True


def mem_create(name, *args):
    template = f'[MemCreate, {name}{{}}]' 
    args = ", ".join(str(i) for i in args)
    if args: 
        args = ", " + args
    return template.format (args)



CLASSES = {
    'memoryview' : mem_create
}


class Analyzer(ast.NodeVisitor):
    def __init__(self, indent = 0, input_file = '', context = None):
        self.input_file = input_file
        self.contents = io.StringIO()
        self.indent = indent
        self.context = context
        self.stack = []
        self.defined = []
        self.zbrush = []
        self.funcs = {}

        if self.context:
            self.input_file = self.context.input_file
            self.defined = self.context.defined
            self.funcs = self.context.funcs

    def format(self):
        "newline separated list, with tabs"
        def yield_values():
            for s in self.stack:
                yield self.tab() + s                
        return '\n'.join(yield_values())

    
    def format_inline(self):
        """ comma separated list"""

        result =  ', '.join(self.stack)
        return result

    def tab(self, extra = 0):
        return '    ' * (self.indent + extra) 

    def visit_Import(self,  node):

        for name in node.names:
            if 'zbrush' in name.name:
                zname = name.name.split(".")[-1]
                self.funcs[name.asname or name.name] = zname

    def visit_ImportFrom(self, node):

        if node.module == 'zbrush':
            for name in node.names:
                self.funcs[name.asname or name.name] = name.name

    def visit_FunctionDef(self, node):

        incoming_args = [j.arg for j in node.args.args]
        arg_string = ', '.join(incoming_args)
        if arg_string:
            arg_string = "\n{}, // args \n{}{}" .format(self.tab(1), self.tab(1), arg_string)

        funcdef = '[RoutineDef, {},\n{{}}{}'.format(node.name, arg_string)
        
        sub_parse = self.sub_parser(*node.body)
        sub_parse.indent = self.indent + 1
        self.stack.append ('')
        self.stack.append ( funcdef.format(sub_parse.format()) )
        self.stack.append ("]")
        self.stack.append ('')

    def visit_Num(self, node):
        self.stack.append( "{}".format(node.n))


    def visit_Interactive(self, node):
        self.generic_visit(node)

    def visit_Str(self, node):
        self.stack.append('\"{}\"'.format(node.s))

    def visit_Name(self, node):
        self.stack.append("[Var, {}]".format(node.id))

    def visit_BinOp(self, node):

        try:
            op = {
                ast.Add: '+',
                ast.Sub:  '-',
                ast.Mult: '*',
                ast.Div:  '/',
                ast.Pow: '^^',
                ast.And:  '&& ',
                ast.Or:   '||'
            }[type(node.op)]

            left = self.sub_parser(node.left)
            right = self.sub_parser(node.right)

            self.stack.append (f"{left.format_inline()} {op} {right.format_inline()}")
        except:
            self.abort("unknown operator", node)

    def visit_AugAssign(self, node):
        op = {
            ast.Add: 'Add',
            ast.Sub: 'Sub',
            ast.Mult: 'Mul',
            ast.Div: 'Div'
        }
        try:
            opstring = op[type(node.op)]
        except:
            self.abort("unknown assigment operator {node.op}", node)

        target_var = node.target.id
        val = node.value

        parser = self.sub_parser(val)
        target_value = parser.format_inline()

        self.stack.append (f'[Var{opstring}, {target_var}, {target_value}]')

        
    def format_mem_op(self, method):
        m_name, _,  m_type = method.partition("_")

        if m_type == 'string':
            return  f'Mem{m_name.title()}String', None

        typecode = {
            'float': 0,
            'char': 1,
            'uchar': 2,
            'short': 3,
            'ushort': 4,
            'long': 5,
            'ulong': 6,
            'fixed': 7
        }.get(m_type, 0)
        return f'Mem{m_name.title()}', typecode


    def visit_Call(self, node):
        
        arg_parser = self.sub_parser(*node.args, func=True)
        arg_string = arg_parser.format_inline()
        if arg_string:
            arg_string = ", " + arg_string

        if isinstance(node.func, ast.Attribute):
            # the only method calls are assumed to be on memory blocks

            m_name, typecode = self.format_mem_op(node.func.attr)
            
            arg_parse = self.sub_parser(*node.args, func=True)
            args = arg_parse.stack
            if typecode:
                args.insert(1, typecode)
            tail  = ''
            if args:
                tail = ", ".join(args)
                tail = ", " + tail

            if 'Write' in m_name:
                self.stack.append(f'[{m_name}, {node.func.value.id}{tail}]')
            else:
                self.stack.append(f'[{m_name}, {node.func.value.id}{tail}]')
            return

        if node.func.id in self.funcs:
            funcname = self.funcs.get(node.func.id) 
            func_string = f'[{funcname}{arg_string}]'
        else:
            func_string = '[RoutineCall, {}{}]' .format(node.func.id, arg_string)
        self.stack.append(func_string)

    def visit_Delete(self, node):
        self.stack.append(f'[MemDelete, {node.targets[0].id}]')

    def visit_Assign(self, node):

        varname = (node.targets[0].id)
        varval = (node.value)

        if isinstance(varval, ast.Num):
            varval = varval.n
        elif isinstance(varval, ast.Str):
            varval = varval.s
        elif isinstance(varval, ast.Name):
            varval = "[Var, {}]".format(varval.id)
        elif isinstance(varval, ast.Call):
            if isinstance(varval.func, ast.Attribute):

                if self.context:
                    setter = 'VarSet'
                else:
                    setter = 'VarDef'

                caller = ", " + varval.func.value.id

                if ("read_" not  in varval.func.attr and varval.func.attr not in self.funcs):
                    self.abort("can only call zbrush functions or memory block functions in an assignment", node)
                
                if varval.func.attr in self.funcs:
                    m_name = varval.func.attr
                    typecode = None
                    caller = ""
                else:
                    # it's a memory object functon
                    m_name, typecode = self.format_mem_op(varval.func.attr)
            
                arg_parse = self.sub_parser(*varval.args, func=True)
                args = arg_parse.stack
                if typecode:
                    args.insert(1, typecode)
                tail  = ''
                if args:
                    tail = ", ".join(args)
                    tail = ", " + tail

               
                
                self.stack.append(f'[{setter}, {varname}, [{m_name}{caller}{tail}]]')
                return

            else:
                formatter = CLASSES.get(varval.func.id, False)
                if formatter:
                    arg_list = []
                    arg_parser = self.sub_parser(*varval.args)
                    arg_list.extend(arg_parser.stack)
                    self.stack.append( formatter(varname, *arg_list))
                    return
                else:
                    self.abort("Can't assign a function call in ZBrush", varval)

        elif isinstance(varval, ast.BinOp):
            parser = self.sub_parser(varval)
            varval = parser.format_inline()
        else:
            self.abort("invalud assignment", varval)
        
        if not self.context and varval not in self.defined:
            setter = f'[VarDef, {varname}, {varval}]'
            self.defined.append(varname)
        else:
            setter = f"[VarSet, {varname}, {varval}]"
        self.stack.append(setter)

    def visit_Lt(self, node):
        self.stack.append (" < ")

    def visit_Gt(self, node):
        self.stack.append (" > ")

    def visit_Lte(self, node):
        self.stack.append (" <=")

    def visit_Gte(self, node):
        self.stack.append (" >= ")

    def visit_Eq(self, node):
        self.stack.append(" = ")  # note, this is not a double equal!

    def visit_NotEq(self, node):
        self.stack.append(" != ")

    
    def visit_If(self, node):

        test = self.sub_parser(node.test)
        comp = ''.join(test.stack)

        body = self.sub_parser(*node.body)
        INDENT = ("\n" + self.tab(1))
        body_str = INDENT.join(body.stack)
        if body_str:
            body_str = f"{INDENT}, // then{INDENT}{body_str}" 

        orelse  = self.sub_parser(*node.orelse)
        else_str = INDENT.join(orelse.stack)
        if else_str:
            else_str = f"{INDENT}, // else{INDENT}{else_str}"

        self.stack.append('')
        self.stack.append(f"[If, {comp}, {body_str}{else_str}")
        self.stack.append(']')
        
    def visit_Expr(self, node):
        sub_parser = self.sub_parser(node.value)
        comp = ''.join(sub_parser.stack)
        self.stack.append(comp)

    def report(self):
        for item in self.stack:
            print (item)


    def abort(self, message, node):
        error_line = self.input_file.splitlines()[node.lineno - 2: node.lineno + 1]
        raise ValueError ("Compile Error: {} in line {}".format(message, node.lineno), error_line )

    def sub_parser(self, *args, **kwargs):
        if kwargs.get('func'):
            sub_parser = FunctionAnalyzer(context = self)
        else:
            sub_parser = Analyzer(context= self)
        sub_parser.indent += 1
        temp = ast.Interactive(list(args))
        sub_parser.visit(temp)
        return sub_parser


class FunctionAnalyzer(Analyzer):

    def visit_Name(self, node):
        self.stack.append(node.id)



def compile(filename):

    

    with open(filename, "r") as source:
        input_file = source.read()
    
    tree = ast.parse(input_file)
    analyzer = Analyzer(0, input_file=input_file)
    analyzer.visit(tree)
    analyzer.report()


    
compile("c:/users/steve/desktop/dummy.py")