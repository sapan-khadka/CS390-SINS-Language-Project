# SINS Interpreter and Control Structures

This folder contains Part 4 of the SINS language project. The interpreter executes programs by traversing the Abstract Syntax Tree produced by the lexer and parser.

## Requirements

- Python 3.10 or later
- No external packages required

## Features

- Variable declarations and assignments
- Environment/symbol table for storing variables
- Arithmetic operators: `+`, `-`, `*`, and `/`
- Correct operator precedence
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, and `>=`
- Print statements
- Multiple statements
- `if/else` control structures
- `while` loops
- Runtime errors for undefined variables, division by zero, and invalid operations
- Meaningful lexer and parser errors

## Project Structure

```text
part4-interpreter/
├── src/
│   ├── __init__.py
│   ├── token_types.py
│   ├── lexer.py
│   ├── ast_nodes.py
│   ├── parser.py
│   ├── environment.py
│   ├── runtime_errors.py
│   └── interpreter.py
├── tests/
│   ├── arithmetic.sins
│   ├── variable.sins
│   ├── comparisons.sins
│   ├── if_else.sins
│   ├── while.sins
│   ├── test_environment.py
│   ├── test_parser.py
│   └── README.md
├── docs/
│   ├── GRAMMAR.ebnf
│   ├── AI_USE_STATEMENT.md
│   └── README.md
├── run_interpreter.py
└── README.md
