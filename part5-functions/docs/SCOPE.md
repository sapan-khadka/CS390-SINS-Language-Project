# Variable Scope

The SINS interpreter represents scope using linked `Environment` objects.

Each environment stores variables declared in its own `_values` dictionary. A
local environment also keeps a reference to its `enclosing` environment. The
enclosing environment may be the global scope or another local scope.

## Variable declaration

`define(name, value)` always creates or replaces a variable in the current
environment. Therefore, a local declaration can shadow a global variable
without changing the global value.

Example:

```text
Global environment: x = 10
Local environment:  x = 20

