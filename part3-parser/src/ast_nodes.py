
class Node:
    """Base class for all AST nodes."""
    pass


class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"ProgramNode(statements={self.statements})"


class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode(value={self.value})"


class VariableNode(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VariableNode(name={self.name})"


class BinaryOpNode(Node):
    """Represents arithmetic and comparison operations."""

    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return (
            f"BinaryOpNode(operator='{self.operator}', "
            f"left={self.left}, right={self.right})"
        )


class AssignmentNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"AssignmentNode(name={self.name}, value={self.value})"


class PrintNode(Node):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"PrintNode(expression={self.expression})"


class BlockNode(Node):
    """Represents statements grouped inside braces."""

    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"BlockNode(statements={self.statements})"


class IfNode(Node):
    """Represents an if statement with an optional else branch."""

    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return (
            f"IfNode(condition={self.condition}, "
            f"then_branch={self.then_branch}, "
            f"else_branch={self.else_branch})"
        )


class WhileNode(Node):
    """Represents a while loop."""

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return (
            f"WhileNode(condition={self.condition}, "
            f"body={self.body})"
        )
