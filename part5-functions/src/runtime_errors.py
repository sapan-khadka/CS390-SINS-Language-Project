"""Runtime errors for the SINS interpreter."""


class SINSRuntimeError(Exception):
    """Base class for errors that occur while executing SINS programs."""


class UndefinedVariableError(SINSRuntimeError):
    """Raised when a program accesses a variable that does not exist."""

    def __init__(self, variable_name: str):
        super().__init__(f"Undefined variable '{variable_name}'")
        self.variable_name = variable_name


class DivisionByZeroError(SINSRuntimeError):
    """Raised when a program attempts to divide by zero."""

    def __init__(self):
        super().__init__("Division by zero")


class InvalidOperationError(SINSRuntimeError):
    """Raised when an operation cannot be performed."""

    def __init__(self, operator: str, left_value, right_value):
        message = (
            f"Invalid operation: {left_value!r} "
            f"{operator} {right_value!r}"
        )
        super().__init__(message)
        self.operator = operator
        self.left_value = left_value
        self.right_value = right_value
