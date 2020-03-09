#zsc.py

import io
import ast
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


WARN_ON_COMPARISONS = True

VERSION = '0.1.0'

class Analyzer(ast.NodeVisitor):
    def __init__(self, indent = 0, input_file = '', context = None):
        self.input_file = input_file
        self.contents = io.StringIO()
        self.indent = indent
        self.context = context
        self.stack = []
        self.defined = []
        self.zbrush = []
        self.funcs = {
            'array' : 'VarDef'
        }

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

    
    def format_inline(self, sep = ", "):
        """ comma separated list"""
        result =  sep.join(self.stack)
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

    def visit_Return(self, node):
        """
        There's not equivalent of 'return values' in zbrush, so abort if the
        python script tries to return values. Otherwise, return an [Exit]
        """
        if node.value:
            self.abort(f"zscript does not support return values", node)
        self.stack.append("[Exit]")

    def visit_Assert(self, node):
        """
        Asserts
        """
        test = self.sub_parser(node.test)
        test_str = test.format_inline(sep=" ")
        self.stack.append(f'[Assert, {test_str}, "{node.msg.s}"]')

    def visit_For(self, node):

        iterator = node.iter
        if not isinstance (iterator, ast.Call) or iterator.func.id not in ('range', 'xrange'):
            self.abort("use range() to set loop iterations", node)
        
        loop_max = iterator.args[0].n
        loop_var = node.target.id

        self.stack.append("")
        self.stack.append(f'[Loop, {loop_max},')
        loop_parser = self.sub_parser(*node.body)

        # loop body
        loop_parser.indent += 1
        self.stack.append(loop_parser.format())
        self.stack.append(self.tab() + ",")
        self.stack.append(self.tab() + f"{loop_var}")
        self.stack.append('] // loop end') 

    def visit_Continue(self, node):
        self.stack.append('[LoopContinue]')

    def visit_Break(self, node):
        self.stack.append('[LoopExit]')

    def visit_FunctionDef(self, node):
        """
        Python def to zbrush [RoutineDef], with indented statements
        and appended in-out arguments
        """
        incoming_args = [j.arg for j in node.args.args]
        arg_string = ', '.join(incoming_args)
        
        self.stack.append ('') # space before defs for readability

        # prepend the docstring
        doc = ast.get_docstring(node)
        if doc: 
            for line in doc.split('\n'):
                self.stack.append(f"// {line} ")


        self.stack.append('[RoutineDef, {},'.format(node.name))
        body_nodes = [e for e in node.body]
        # docstring will appear as an expression node
        # if present
        if doc:
            body_nodes = body_nodes[1:]
        sub_parse = self.sub_parser(*body_nodes)
        sub_parse.indent = self.indent + 1
        self.stack.append ( sub_parse.format())    
    
        if arg_string:        
            self.stack.append(f'{self.tab(1)}, // args ')
            self.stack.append(f'{self.tab(1)}{arg_string}')
        self.stack.append (f"] // end {node.name}")
        self.stack.append ('')

    def visit_Num(self, node):
        """
        numeric literals
        """
        self.stack.append( "{}".format(node.n))

    def visit_Interactive(self, node):
        """"
        won't show up in raw code, used as a generic node
        container for sub-parsers
        """
        self.generic_visit(node)

    def visit_Str(self, node):
        """
        Make sure string literals have quotes
        """
        self.stack.append('\"{}\"'.format(node.s))

    def visit_Name(self, node):
        """
        Convert python name refereences to [Var, name]
        """
        # Q: when to use 'Val' instead?
        # Q: should we use #character?

        self.stack.append("[Var, {}]".format(node.id))

    def visit_BinOp(self, node):
        '''
        Format zbrush supported math operators
        '''
        # Q: Do we want 'val' instead of 'var' here?
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

            self.stack.append (f"({left.format_inline(sep= ' ')} {op} {right.format_inline(sep = ' ')})")
        except:
            self.abort("ZBrush does not support operator {}".format(node.op), node)

    def visit_BoolOp(self, node):
                
    
        op = {
            ast.Or: '||',
            ast.And:  '&& '
        }[type(node.op)]

        left = self.sub_parser(node.values[0])
        right = self.sub_parser(node.values[1])

        self.stack.append (f'({left.format_inline(sep = " ")} {op} {right.format_inline(sep = " ")})')
    

    def visit_AugAssign(self, node):
        '''
        Convert python augmented assigns like

            variable += 5

        to

            [VarAdd, variable, 5]

        etc
        '''
        
        op = {
            ast.Add: 'Add',
            ast.Sub: 'Sub',
            ast.Mult: 'Mul',
            ast.Div: 'Div'
        }
        try:
            opstring = op[type(node.op)]
        except:
            self.abort("ZBrush does not support augmented operator {}".format(node.op), node)

        target_var = node.target.id
        val = node.value

        parser = self.sub_parser(val)
        target_value = parser.format_inline()

        self.stack.append (f'[Var{opstring}, {target_var}, {target_value}]')

        
    def format_mem_op(self, method):
        '''
        helper method convert, eg, 
            
            some_mem_block.read_string(offset)

        to

            [MemReadString, some_mem_block, offset]

        or 

            some_mem_block.write_ulong(value)

        to 

            [MemWrite, some_mem_block, value, 6]

        where '6' is the zbrush typecode for ulongs

        '''

        m_name, _,  m_type = method.partition("_")

        if m_name not in  ('read', 'write', 'resize', 'move', 'delete', 'multi_write', 'create_from_file'):
            return None, None

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

        is_attrib = isinstance(node.func, ast.Attribute)
        is_zb = False  # is this a recognized call
        is_mem_call = False
  
        if is_attrib:
            owner_name = node.func.value.id
            func_name = node.func.attr
            is_mem_call = (owner_name != "zbrush")
        else:
            owner_name = ""
            func_name = node.func.id

        is_zb = owner_name == 'zbrush' or func_name in self.funcs

        # collect the arguments              
        arg_parser = self.sub_parser(*node.args, func=True)
        arg_string = arg_parser.format_inline()
        if arg_string:
            arg_string = ", " + arg_string

        if is_zb:
            # it's a zbrush function.  de-alias in possible and return
            if func_name in self.funcs:
                func_name = self.funcs.get(node.func.id, func_name) 
    
            func_string = f'[{func_name}{arg_string}]'
            self.stack.append(func_string)
            return

        if not is_mem_call:
            # it's not a zbrush call or a memblock function,
            # so we assume it's a routine call
            func_string = '[RoutineCall, {}{}]' .format(func_name, arg_string)
            self.stack.append(func_string)
            return

        else:
            # this is an operation on a mem block
            m_name, typecode = self.format_mem_op(func_name)
            if not m_name:
                # this will fail on, eg, a random python imported function
                self.abort(f"Unrecognized operation {owner_name}.{func_name}",  node)
            
            # we have to insert the appropriate type code for value types here
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

                is_mem_create = varval.func.attr == 'MemCreate'

                if is_mem_create:
                    arg_parser = self.sub_parser(*varval.args)
                    arg_string = arg_parser.format_inline()
                    if arg_string:
                        arg_string = ", " + arg_string
                    
                    self.stack.append(f'[MemCreate, {varname}{arg_string}]') 
                    return

                allowed_funcs = (
                    "read_",
                )

                is_allowed = False
                for f in allowed_funcs:
                    is_allowed = is_allowed or  f in varval.func.attr

                if (not is_allowed and varval.func.attr not in self.funcs):
                    self.abort("can only call zbrush functions or memory block functions in an assignment", node)
                
                if varval.func.attr in self.funcs:
                    m_name = varval.func.attr
                    typecode = None
                    caller = ""
                else:
                    # it's a memory object functon
                    m_name, typecode = self.format_mem_op(varval.func.attr)
                    if not m_name:
                        self.abort(f"Unrecognized memory operation {varval.func.attr}",  node)
            
                arg_parse = self.sub_parser(*varval.args, func=True)
                args = arg_parse.stack
                if typecode:
                    args.insert(1, typecode)
                tail  = ''
                if args:
                    tail = ", ".join(args)
                    tail = ", " + tail

                if  m_name.lower() == 'array':
                    # we simulate array assignments with 'zbrush.array( count, fill value)'
                    try:
                        count = arg_parse.stack[0]
                    except:
                        count = 1
                    try:
                        fill = arg_parse.stack[1]
                    except:
                        fill = ''
                    if fill:
                        fill = f", {fill}"

                    self.stack.append(f'[{setter}, {varname}({count}){fill}]')
                else:
                    self.stack.append(f'[{setter}, {varname}, [{m_name}{caller}{tail}]]')
                return

            self.abort("Can't assign a function call in ZBrush", varval)

        elif isinstance(varval, ast.BinOp):
            parser = self.sub_parser(varval)
            varval = parser.format_inline()
        # elif isinstance (varval, ast.Tuple) or isinstance(varval, ast.List):
        #     values = self.sub_parser(*varval.elts)
        #     cnt = values.stack.pop()
        #     try:
        #         example = values.stack.pop()
        #     except: 
        #         example = ''
        #     if example:
        #         example = ", " + example
            
        #     self.stack.append(f'[VarDef, {varname}({cnt}){example}]')
        #     return
        else:
            self.abort("invalid assignment", varval)
        
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
        if isinstance(node.value, ast.Str):
            self.stack.append(f'// {node.value.s}')
        else:
            sub_parser = self.sub_parser(node.value)
            comp = ''.join(sub_parser.stack)
            self.stack.append(comp)

    def report(self):
        for item in self.stack:
            print (item)


    def abort(self, message, node):
        """
        fail the transpilation and print an error message
        """

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



def compile(filename, out_filename = ''):


    with open(filename, "r") as source:
        input_file = source.read()
    
    tree = ast.parse(input_file)
    analyzer = Analyzer(0, input_file=input_file)
    analyzer.visit(tree)

    out_filename = out_filename or filename.replace('.py', '.txt')

    with open(out_filename, 'wt') as output:
        tp = (f'transpiled with zsc {VERSION}')
        orig = f'from: {filename}'

        output.write(f"/*\n{tp}\n{orig}\n*/\n\n")
        output.write(analyzer.format())

    print (analyzer.format())
    
compile("c:/users/steve/desktop/dummy.py")