
from .ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    AssignmentNode,
    PrintNode,
    BlockNode,
    IfNode,
    WhileNode,
)
from .environment import Environment


class InterpreterError(Exception):
    """Raised when a runtime error occurs."""


class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def interpret(self, program):
        self._execute(program)

    def _execute(self, node):
        if isinstance(node, (ProgramNode, BlockNode)):
            for statement in node.statements:
                self._execute(statement)

        elif isinstance(node, AssignmentNode):
            value = self._evaluate(node.value)
            is_declaration = getattr(node, "is_declaration", False)

            if is_declaration:
                if node.name in self.environment.variables:
                    raise InterpreterError(
                        f"Variable already declared: '{node.name}'"
                    )
                self.environment.define(node.name, value)
            else:
                self.environment.assign(node.name, value)

        elif isinstance(node, PrintNode):
            print(self._evaluate(node.expression))

        elif isinstance(node, IfNode):
            if self._condition(node.condition):
                self._execute(node.then_branch)
            elif node.else_branch is not None:
                self._execute(node.else_branch)

        elif isinstance(node, WhileNode):
            while self._condition(node.condition):
                self._execute(node.body)

        else:
            raise InterpreterError(
                f"Unsupported statement: {type(node).__name__}"
            )

    def _evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, VariableNode):
            try:
                return self.environment.get(node.name)
            except RuntimeError as error:
                raise InterpreterError(str(error)) from error

        if isinstance(node, BinaryOpNode):
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            op = node.operator

            if op in ("+", "-", "*", "/"):
                if type(left) not in (int, float) or type(right) not in (int, float):
                    raise InterpreterError(
                        f"Invalid arithmetic operands for '{op}'"
                    )

                if op == "+":
                    return left + right
                if op == "-":
                    return left - right
                if op == "*":
                    return left * right
                if op == "/":
                    if right == 0:
                        raise InterpreterError("Division by zero")
                    return left / right

            if op in ("==", "!=", "<", ">", "<=", ">="):
                if op in ("<", ">", "<=", ">="):
                    if type(left) not in (int, float) or type(right) not in (int, float):
                        raise InterpreterError(
                            f"Invalid comparison operands for '{op}'"
                        )

                if op == "==":
                    return left == right
                if op == "!=":
                    return left != right
                if op == "<":
                    return left < right
                if op == ">":
                    return left > right
                if op == "<=":
                    return left <= right
                if op == ">=":
                    return left >= right

            raise InterpreterError(f"Unsupported operator: '{op}'")

        raise InterpreterError(
            f"Unsupported expression: {type(node).__name__}"
        )

    def _condition(self, node):
        result = self._evaluate(node)
        if type(result) is not bool:
            raise InterpreterError(
                "Condition must evaluate to true or false"
            )
        return result
