#!/usr/bin/env python3

__author__ = ['J. Sebastian', '[Brandon Amos](https://github.com/bamos)']
__date__ = '2013.08.01'

"""
A module to evaluate a mathematical expression using Python's AST.

+ Original by: J. Sebastian at http://stackoverflow.com/questions/2371436.
+ Modifications by: [Brandon Amos](https://github.com/bamos).

If you want a command-line expression evaluator, use
[Russell91/pythonpy](https://github.com/Russell91/pythonpy).


```
$ eval-expr.py '(((4+6)*10)<<2)'
(((4+6)*10)<<2) = 400
```
"""

import ast
import operator as op


class EvalExpr:
    def __init__(self, varMap):
        self.ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                    ast.Div: op.truediv, ast.Mod: op.mod, ast.Pow: op.pow,
                    ast.LShift: op.lshift, ast.RShift: op.rshift,
                    ast.BitOr: op.or_, ast.BitXor: op.xor, ast.BitAnd: op.and_,
                    ast.FloorDiv: op.floordiv, ast.Invert: op.invert,
                    ast.Not: op.not_, ast.UAdd: op.pos, ast.USub: op.neg}
        self.varMap = varMap

    def evalExpr(self, expr):
        return self.__eval(ast.parse(expr).body[0].value)

    def __eval(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif type(node) in self.ops:
            return self.ops[type(node)]
        elif isinstance(node, ast.UnaryOp):
            return self.__eval(node.op)(self.__eval(node.operand))
        elif isinstance(node, ast.BinOp):
            return self.__eval(node.op)(self.__eval(node.left),
                                        self.__eval(node.right))
        elif node.id in self.varMap:
            return self.varMap[node.id]
        else:
            raise TypeError(node)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        expr = sys.argv[1]
        print(expr + " = " + str(EvalExpr({}).evalExpr(expr)))
    else:
        print("Usage: ./EvalExpr.py <mathematical expression>")
