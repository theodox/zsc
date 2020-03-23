import ast
import inspect
from . import zbrush

class ParseError (ValueError):
    pass

class Prepass(ast.NodeVisitor):
    """
    This runs a prepass which collects all function calls,
    so we know which ones have been defined and which ones
    are zbrush-native
    """

    ALLOWED_MODULES = 'math', 'zbrush', 'zsc', 'random'

    def __init__(self):
        self.user_functions = {}
        self.zbrush_functions = {}
        self.zbrush_aliases = {
            "sin": "SIN",
            "cos": "COS",
            "tan": "TAN",
            "asin": "ASIN",
            "acos": "ACOS",
            "atan": "ATAN",
            "atan2": "ATAN2",
            "log": "LOG",
            "log10": "LOG10",
            "sqrt": "SQRT",
            "abs": "ABS",
            "random": "RAND",
            "randint": "IRAND",
            "bool": "BOOL",
            "int": "INT",
            "frac": "FRAC",
            'min': 'MIN',
            'max': 'MAX'
        }

        for k, v in inspect.getmembers(zbrush):
            if (not "_" in k) and callable(v):
                self.zbrush_aliases[k] = k
                self.zbrush_functions[k] = inspect.getfullargspec(v)

        self.math_imports = {("sin", "cos", "tan", "asin", "acos",
                              "atan", "atan2", "log", "log10", "sqrt", "abs")}
        self.random_imports = {('random', 'randint')}
        self.intrinsics = {('max', 'min', 'len', 'abs', 'bool', 'int', 'float', 'frac')}

    def get_call_name(self, node):
        if (not isinstance(node, ast.Call)):
            return '', '', ''
        try:
            prefix = ''
            name = node.func.id
        except:
            prefix = node.func.value.id
            name = node.func.attr

        alias = self.zbrush_aliases.get(name, '')
        if not alias and prefix == 'zbrush':
            alias = name
        return prefix, name, alias

    def visit_Import(self,  node):
        """
        Raise on illegal imports
        """
        for mod in node.names:
            print ("import", mod.name, mod.asname)
            name = mod.name.split(".")[0]
            if name not in self.ALLOWED_MODULES:
                raise ParseError(
                    f"Illegal import '{name}' in line {node.lineno}.  Supported imports are {self.ALLOWED_MODULES}")

    def visit_ImportFrom(self, node):
        """
        Raise on illegal imports
        """
        if node.module not in self.ALLOWED_MODULES:
            raise ParseError(
                f"Illegal import '{node.module}' in line {node.lineno}.  Supported imports are {self.ALLOWED_MODULES}")

        if node.module == 'zbrush' or 'zsc.zbrush':
            allowed_names = self.zbrush_functions
        elif node.module == 'math':
            allowed_names = self.math_imports
        elif node.module == 'random':
            allowed_names = self.random_imports
        
        for name in node.names:
            print ("importfrom", name.name, name.asname)
            if name.name not in allowed_names:
                raise ParseError(f"Unrecognized import '{name.name}' from module '{node.module}' in line {node.lineno}")
            if name.asname and node.module in ('zbrush', 'zsc.zbrush'):
                self.zbrush_aliases[name.asname] = name.name

    def visit_FunctionDef(self, node):
        """
        Save an argSpec for user defined functions
        """
        args = [a.arg for a in node.args.args]
        if node.args.kwonlyargs:
            raise ParseError(f"Keyword-only arguments not supported in Zbursh: def {node.name}, line {node.lineno}")
        if node.args.vararg:
            raise ParseError(f"Variable arguments not supported in Zbursh: def {node.name}, line {node.lineno}")
        if node.args.kw_defaults:
            raise ParseError(f"keyword default arguments not supported in Zbrush: def {node.name}, line {node.lineno}")
        if node.args.defaults:
            raise ParseError(f"default arguments not supported in Zbrush: def {node.name}, line {node.lineno}")
        if node.args.kwarg:
            raise ParseError(f"keyword arguments not allowed in Zbrush user : def {node.name}, line {node.lineno}")

        self.user_functions[node.name] = inspect.FullArgSpec(args = args, varargs = None, varkw=None,  defaults=None, kwonlyargs=None,  kwonlydefaults=None, annotations = {})

    def visit_Call(self, node):
            
        prefix, name, alias = self.get_call_name(node)

        if name in self.user_functions:
            expected =  len(self.user_functions[name].args)
            got = len(node.args)
            if got != expected:
                raise ParseError(f"Function {name} requires {expected} arguments, was called with {got} in line {node.lineno}")

        if prefix in ('zbrush', 'zsc.zbrush'):
            if name not in self.zbrush_functions and alias not in self.zbrush_functions:
                raise ParseError(f"{alias or name} is not a Zbrush function: line {node.lineno}")

        if name in self.zbrush_functions or alias in self.zbrush_functions:
            # todo : here's where we ensure that the zbrush func signature is respected
            # defaults = 0
            # if self.zbrush_functions[name].defaults:
            #     defaults = len(self.zbrush_functions[name].defaults)
            # print ("called", name, alias, len(node.args), len(self.zbrush_functions[name].args), defaults)
            pass


    def is_zbrush_function(self, node):
        prefix, name, alias = self.get_call_name(node)
        return name in self.zbrush_aliases or alias in self.zbrush_aliases

    def is_user_function(self, node):
        prefix, name, alias = self.get_call_name(node)
        return name not in self.zbrush_aliases and name in self.user_functions

    def get_zbrush_func(self, node):    
        prefix, name, alias = self.get_call_name(node)

        
