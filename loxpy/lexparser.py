class Expr:
    left = None
    operator = None
    right = None
    
    
class BinaryExpr(Expr):
    def __init__(self, left, operator, right):
        assert left
        assert operator
        assert right
        self.left = left
        self.operator = operator
        self.right = right

class GroupingExpr(Expr):
    def __init__(self, expression):
        assert expression
        self.expr = expression

class LiteralExpr(Expr):
    def __init__(self, value):
        assert value
        self.value = value

class UnaryExpr(Expr):
    def __init__(self, operator, right):
        assert operator
        assert right
        self.operator = operator
        self.right = right

class ASTPrinter:
    @staticmethod
    def print(expression):
        pass
    
    def visitBinaryExpr(self):
        pass

    def visitGroupingExpr(self):
        pass

    def visitLiteralExpr(self):
        pass

    def visitUnaryExpr(self):
        pass

    
