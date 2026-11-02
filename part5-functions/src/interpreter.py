
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
    FunctionDefinitionNode,
    FunctionCallNode,
    ReturnNode,
    StringNode,
)
from .environment import Environment
from .runtime_errors import (
    SINSRuntimeError,
    DivisionByZeroError,
    InvalidOperationError,
    UndefinedFunctionError,
    ArgumentCountError,
    ReturnOutsideFunctionError,
)

InterpreterError = SINSRuntimeError


class ReturnSignal(Exception):
    """Internal signal used to return a value from a function."""

    def __init__(self, value):
        self.value = value


class Interpreter:
    def __init__(self, environment=None):
        self.environment = (
            environment if environment is not None else Environment()
        )
        self.functions = {}
        self.function_depth = 0

    def interpret(self, program):
        if not isinstance(program, ProgramNode):
            raise TypeError("Expected a ProgramNode")

        self._execute(program)
        return self.environment.snapshot()

    def execute(self, node):
        return self._execute(node)

    def evaluate(self, node):
        return self._evaluate(node)

    def _execute(self, node):
        if isinstance(node, ProgramNode):
            for statement in node.statements:
                self._execute(statement)
            return

        if isinstance(node, BlockNode):
            for statement in node.statements:
                self._execute(statement)
            return

        if isinstance(node, FunctionDefinitionNode):
            self.functions[node.name] = (
                node,
                self.environment
            )
            return

        if isinstance(node, FunctionCallNode):
            self._evaluate(node)
            return

        if isinstance(node, ReturnNode):
            if self.function_depth == 0:
                raise ReturnOutsideFunctionError()

            value = self._evaluate(node.value)
            raise ReturnSignal(value)

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

        if isinstance(node, IfNode):
            condition = self._evaluate(node.condition)
            self._check_condition(condition)

            if condition:
                self._execute(node.then_branch)
            elif node.else_branch is not None:
                self._execute(node.else_branch)
            return

        if isinstance(node, WhileNode):
            while True:
                condition = self._evaluate(node.condition)
                self._check_condition(condition)

                if not condition:
                    break

                self._execute(node.body)
            return

        raise SINSRuntimeError(
            f"Unsupported statement: {type(node).__name__}"
        )

    def _evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, StringNode):
            return node.value

        if isinstance(node, VariableNode):
            return self.environment.get(node.name)

        if isinstance(node, FunctionCallNode):
            return self._call_function(node)

        if isinstance(node, BinaryOpNode):
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            operator = node.operator

            if operator in ("==", "!=", "<", "<=", ">", ">="):
                return self._evaluate_comparison(operator, left, right)

            if operator in ("+", "-", "*", "/"):
                return self._evaluate_arithmetic(operator, left, right)

            raise InvalidOperationError(operator, left, right)

        raise SINSRuntimeError(
            f"Unsupported expression: {type(node).__name__}"
        )

    def _call_function(self, call):
        if call.name not in self.functions:
            raise UndefinedFunctionError(call.name)

        definition, defining_environment = self.functions[call.name]

        if len(call.arguments) != len(definition.parameters):
            raise ArgumentCountError(
                call.name,
                len(definition.parameters),
                len(call.arguments)
            )

        arguments = [
            self._evaluate(argument)
            for argument in call.arguments
        ]

        previous_environment = self.environment
        self.environment = defining_environment.create_child()

        for parameter, argument in zip(
            definition.parameters, arguments
        ):
            self.environment.define(parameter, argument)

        self.function_depth += 1

        try:
            self._execute(definition.body)
        except ReturnSignal as result:
            return result.value
        finally:
            self.environment = previous_environment
            self.function_depth -= 1

        return None

    def _evaluate_arithmetic(self, operator, left, right):
        if operator == "+" and (
            isinstance(left, str) or isinstance(right, str)
        ):
            return str(left) + str(right)

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

    def _evaluate_comparison(self, operator, left, right):
        if operator in ("==", "!="):
            return (
                left == right
                if operator == "=="
                else left != right
            )

        if (
            isinstance(left, bool)
            or isinstance(right, bool)
            or not isinstance(left, (int, float))
            or not isinstance(right, (int, float))
        ):
            raise InvalidOperationError(operator, left, right)

        if operator == "<":
            return left < right

        if operator == "<=":
            return left <= right

        if operator == ">":
            return left > right

        if operator == ">=":
            return left >= right

        raise InvalidOperationError(operator, left, right)

    @staticmethod
    def _check_condition(value):
        if not isinstance(value, bool):
            raise SINSRuntimeError(
                "Condition must evaluate to True or False"
            )
