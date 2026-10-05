class Node:
    """Base class for all nodes."""
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
