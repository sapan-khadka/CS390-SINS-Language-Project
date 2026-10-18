"""Variable environment for the SINS interpreter."""

from .runtime_errors import UndefinedVariableError


class Environment:
    """Stores and retrieves variables during program execution."""

    def __init__(self):
        self._values = {}

    def define(self, name: str, value):
        """Create a variable or replace an existing declaration."""
        self._values[name] = value
        return value

    def assign(self, name: str, value):
        """Update a variable that has already been declared."""
        if name not in self._values:
            raise UndefinedVariableError(name)

        self._values[name] = value
        return value

    def get(self, name: str):
        """Return the value stored for a variable."""
        if name not in self._values:
            raise UndefinedVariableError(name)

        return self._values[name]

    def contains(self, name: str) -> bool:
        """Return whether a variable exists."""
        return name in self._values

    def snapshot(self) -> dict:
        """Return a copy of the current symbol table."""
        return dict(self._values)
