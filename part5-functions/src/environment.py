"""Variable environments for the SINS interpreter."""

from .runtime_errors import UndefinedVariableError


class Environment:
    """Stores variables in one scope with an optional parent scope."""

    def __init__(self, enclosing=None):
        self._values = {}
        self.enclosing = enclosing

    def define(self, name: str, value):
        """Create or replace a variable in the current scope."""
        self._values[name] = value
        return value

    def assign(self, name: str, value):
        """Update the nearest scope containing the variable."""
        if name in self._values:
            self._values[name] = value
            return value

        if self.enclosing is not None:
            return self.enclosing.assign(name, value)

        raise UndefinedVariableError(name)

    def get(self, name: str):
        """Retrieve a variable from the nearest available scope."""
        if name in self._values:
            return self._values[name]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise UndefinedVariableError(name)

    def contains(self, name: str) -> bool:
        """Return whether the variable exists in this scope chain."""
        if name in self._values:
            return True

        if self.enclosing is not None:
            return self.enclosing.contains(name)

        return False

    def contains_local(self, name: str) -> bool:
        """Return whether the variable exists in only this scope."""
        return name in self._values

    def create_child(self):
        """Create a local environment whose parent is this environment."""
        return Environment(enclosing=self)

    def snapshot(self) -> dict:
        """Return a copy of variables defined in the current scope."""
        return dict(self._values)
