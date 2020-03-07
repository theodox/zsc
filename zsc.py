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

KNOWN = {
    'Note' : '[Note{}]'
}

class Analyzer(ast.NodeVisitor):
    def __init__(self, indent = 0, input_file = '', context = None):
        self.input_file = input_file
        self.contents = io.StringIO()
        self.indent = indent
        self.context = context
        self.stack = []
        self.defined = []

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

    def visit_FunctionDef(self, node):

        incoming_args = [j.arg for j in node.args.args]
        arg_string = ', '.join(incoming_args)
        if arg_string:
            arg_string = "\n{}, // args \n{}{}" .format(self.tab(1), self.tab(1), arg_string)

        funcdef = '[RoutineDef, {},\n{{}}{}\n]'.format(node.name, arg_string)
        
        b = ast.Interactive([i for i in node.body])
        v = Analyzer(1, input_file=self.input_file, context=node)
        v.defined = incoming_args
        v.visit(b)
        contents = v.format()

        self.stack.append (funcdef.format(contents))

    def visit_Num(self, node):
        self.stack.append( " {} ".format(node.n))

    def visit_Interactive(self, node):
        self.generic_visit(node)

    def visit_Str(self, node):
        self.stack.append(' \"{}\" '.format(node.s))

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

            left = ast.Interactive([node.left])
            L = Analyzer(input_file=self.input_file, context = node)
            L.visit(left)

            right = ast.Interactive([node.right])
            R = Analyzer(input_file=self.input_file, context = node)
            R.visit(right)

            self.stack.append (f"{L.format_inline()} {op} {R.format_inline()}")
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
        parser = ast.Interactive([val])
        v = Analyzer(0, self.input_file, context=node)
        v.visit(parser)
        target_value = v.format_inline()

        self.stack.append (f'[Var{opstring}, {target_var}, {target_value}]')

        
    def visit_Call(self, node):
        args = []
        for each_arg in node.args:
            b = ast.Interactive([each_arg])
            v = FunctionAnalyzer()
            v.visit(b)
            args.extend(v.stack)

        arg_string = ', '.join(args)
        if arg_string:
            arg_string =  ", " +  arg_string

        if isinstance(node.func, ast.Attribute):
            # this is a method called on a memblock
            method = node.func.attr
            m_name, _,  m_type = method.partition("_")
            _s = ''
            typecode = ''
            offset = ''
            if len(node.args) > 1:
                offset = f', {node.args[1].n}'
            if m_type == 'string':
               _s = "String"
            m_name = f'Mem{m_name.title()}{_s}'
            if not _s:
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

                typecode = f", {typecode}" 

            if m_name == 'write':
                self.stack.append(f'[{m_name}, {node.func.value.id}, {node.args[0].n}{typecode}{offset}]')
            else:
                self.stack.append(f'[{m_name}, {node.func.value.id}, {typecode}{offset}]')
            return

        if node.func.id in KNOWN:
            func_string = KNOWN[node.func.id].format(arg_string)
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
                parse_call = ast.Interactive([varval])
                v  = FunctionAnalyzer(0, self.input_file, varval.func.attr)
                v.visit(parse_call)
                parsed = v.stack.pop()
                if not 'Read' in parsed:
                    self.abort('can only assign to a MemRead call', node)


                parse_args = ast.Interactive(varval.args)
                a  = FunctionAnalyzer(0, self.input_file, varval.func.attr)
                a.visit(parse_args)
                parsed = a.format_inline()
                self.stack.append(parsed)
                
                
                self.stack.append(parsed)
                return


            else:
                formatter = CLASSES.get(varval.func.id, False)
                if formatter:
                    arg_list = []
                    arg_parser = ast.Interactive(varval.args)
                    v = Analyzer()
                    v.visit(arg_parser)
                    arg_list.extend(v.stack)
                    self.stack.append( formatter(varname, *arg_list))
                    return
                else:
                    self.abort("Can't assign a function call in ZBrush", varval)
        elif isinstance(varval, ast.BinOp):

            parser = ast.Interactive([varval])
            v = Analyzer(input_file=self.input_file, context= self)
            v.visit(parser)
            varval = v.format_inline()
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
        b = ast.Interactive([node.test])
        v = Analyzer(0, input_file=self.input_file, context=node)
        v.visit(b)
        comp = ''.join(v.stack)

        body = ast.Interactive(node.body)
        v2 = Analyzer(context=node)
        v2.visit(body)
        INDENT = ("\n" + self.tab(1))
        body_str = INDENT.join(v2.stack)
        if body_str:
            body_str = f"{INDENT}, // then{INDENT}{body_str}" 

        orelse = ast.Interactive(node.orelse )
        v2 = Analyzer()
        v2.visit(orelse)
        else_str = INDENT.join(v2.stack)
        if else_str:
            else_str = f"{INDENT}, // else{INDENT}{else_str}"

        self.stack.append(f"[If, {comp}, {body_str}{else_str}\n]")
        
    def visit_Expr(self, node):
        b = ast.Interactive([node.value])
        v = Analyzer()
        v.visit(b)
        comp = ''.join(v.stack)
        self.stack.append(comp)

    def report(self):
        for item in self.stack:
            print (item)


    def abort(self, message, node):
        error_line = self.input_file.splitlines()[node.lineno - 2: node.lineno + 1]
        raise ValueError ("Compile Error: {} in line {}".format(message, node.lineno), error_line )


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