class Environment:
    """Stores variable names and their current values."""

    def __init__(self):
        self.variables = {}

    def define(self, name, value):
        """Create or initialize a variable."""
        self.variables[name] = value

    def get(self, name):
        """Retrieve a variable's value."""
        if name not in self.variables:
            raise RuntimeError(
                f"Undefined variable: '{name}'"
            )
        return self.variables[name]

    def assign(self, name, value):
        """Update an existing variable."""
        if name not in self.variables:
            raise RuntimeError(
                f"Undefined variable: '{name}'"
            )
        self.variables[name] = value

    def __repr__(self):
        return f"Environment({self.variables})"
