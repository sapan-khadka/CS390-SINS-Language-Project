# SINS Interpreter — Part 5

This folder contains the complete Part 5 SINS interpreter. It extends the Part 4 interpreter with user-defined functions, nested variable scope, and strings as the additional language feature.

## Requirements

- Python 3.10 or later
- No external packages

## Supported Features

- Variable declarations and assignments
- Numeric and string values
- Arithmetic with precedence: `+`, `-`, `*`, `/`
- String concatenation with `+`, including mixed string and numeric values
- String escape sequences: `\'`, `\\`, `\n`, and `\t`
- Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`
- `print`, `if/else`, and `while`
- Function definitions and calls
- Parameters and return values
- Function-local variables
- Global and local scope with variable shadowing
- Runtime errors for invalid operations, undefined names, incorrect argument counts, division by zero, and invalid returns

## Function Example

```sins
func add(a, b) {
    return a + b;
}

let result = add(10, 20);
print(result);
```

## Scope Representation

Each `Environment` stores variables for one scope and may reference an enclosing environment. A function call creates a child environment. Parameters and local declarations are stored in that child. Variable lookup walks outward to the nearest enclosing scope, while declarations remain local. This allows a local variable to shadow a global variable without changing it.

## Running the Interpreter

Run commands from this directory:

```bash
python3 run_interpreter.py tests/function_test.sins
python3 run_interpreter.py tests/scope_shadowing.sins
python3 run_interpreter.py tests/local_variables.sins
python3 run_interpreter.py tests/function_no_parameters.sins
python3 run_interpreter.py tests/strings.sins
```

Run the automated tests with:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Part 5 Test Programs

1. `function_test.sins` — parameters, return values, and function calls
2. `scope_shadowing.sins` — global and local variable shadowing
3. `local_variables.sins` — function-local calculation
4. `function_no_parameters.sins` — a function with no parameters returning a string
5. `strings.sins` — strings, escapes, and concatenation

## Project Structure

```text
part5-functions/
├── src/
│   ├── ast_nodes.py
│   ├── environment.py
│   ├── interpreter.py
│   ├── lexer.py
│   ├── parser.py
│   ├── runtime_errors.py
│   └── token_types.py
├── tests/
├── docs/
│   ├── AI_USE_STATEMENT.md
│   ├── GRAMMAR.ebnf
│   └── SCOPE.md
├── run_interpreter.py
├── run_parser.py
└── README.md
```
