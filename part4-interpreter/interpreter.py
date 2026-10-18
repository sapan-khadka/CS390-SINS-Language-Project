
"""Interpreter for the SINS programming language."""

from .ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    AssignmentNode,
    PrintNode,
)
from .environment import Environment
from .runtime_errors import (
    SINSRuntimeError,
    UndefinedVariableError,
    DivisionByZeroError,
    InvalidOperationError,
)

# Keep compatibility with run_parser.py.
InterpreterError = SINSRuntimeError


class Interpreter:
    """Executes SINS abstract syntax trees."""

    def __init__(self):
        self.environment = Environment()

    def interpret(self, program):
        """Execute a complete program."""
        self._execute(program)

    def _execute(self, node):
        if isinstance(node, ProgramNode):
            for statement in node.statements:
                self._execute(statement)
            return

        if isinstance(node, AssignmentNode):
            value = self._evaluate(node.value)

            if getattr(node, "is_declaration", False):
                self.environment.define(node.name, value)
            else:
                self.environment.assign(node.name, value)
            return

        if isinstance(node, PrintNode):
            print(self._evaluate(node.expression))
            return

        # Support BlockNode, IfNode, and WhileNode once added to the AST.
        node_type = type(node).__name__

        if node_type == "BlockNode":
            for statement in node.statements:
                self._execute(statement)
            return

        if node_type == "IfNode":
            condition = self._evaluate(node.condition)
            self._check_condition(condition)

            if condition:
                self._execute(node.then_branch)
            elif node.else_branch is not None:
                self._execute(node.else_branch)
            return

        if node_type == "WhileNode":
            while True:
                condition = self._evaluate(node.condition)
                self._check_condition(condition)
                if not condition:
                    break
                self._execute(node.body)
            return

        raise SINSRuntimeError(
            f"Unsupported statement: {node_type}"
        )

    def _evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, VariableNode):
            return self.environment.get(node.name)

        if isinstance(node, BinaryOpNode):
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            operator = node.operator

            if operator in ("==", "!=", "<", "<=", ">", ">="):
                try:
                    if operator == "==":
                        return left == right
                    if operator == "!=":
                        return left != right
                    if operator == "<":
                        return left < right
                    if operator == "<=":
                        return left <= right
                    if operator == ">":
                        return left > right
                    if operator == ">=":
                        return left >= right
                except TypeError:
                    raise InvalidOperationError(
                        operator, left, right
                    ) from None

            if (
                isinstance(left, bool)
                or isinstance(right, bool)
                or not isinstance(left, (int, float))
                or not isinstance(right, (int, float))
            ):
                raise InvalidOperationError(operator, left, right)

            if operator == "+":
                return left + right
            if operator == "-":
                return left - right
            if operator == "*":
                return left * right
            if operator == "/":
                if right == 0:
                    raise DivisionByZeroError()
                return left / right

            raise InvalidOperationError(operator, left, right)

        raise SINSRuntimeError(
            f"Unsupported expression: {type(node).__name__}"
        )

    @staticmethod
    def _check_condition(value):
        if not isinstance(value, bool):
            raise SINSRuntimeError(
                "Condition must evaluate to True or False"
            )
