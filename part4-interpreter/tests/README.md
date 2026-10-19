# SINS Language — Part 4: Interpreter

## Overview

This project implements an interpreter for the SINS programming language. It builds on the lexer and parser to execute programs containing variables, arithmetic expressions, comparisons, print statements, conditional branches, and loops.

## Features

- Variable declarations using `let`.
- Assignment to previously declared variables.
- Arithmetic operations: `+`, `-`, `*`, `/`.
- Arithmetic precedence and parentheses.
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- `print(expression);` statements.
- `if`/`else` conditional statements.
- `while` loops.
- Runtime errors for undefined variables, division by zero, and invalid operations.

## Project Structure

- `src/ast_nodes.py` — abstract syntax tree node definitions.
- `src/environment.py` — variable storage and lookup.
- `src/interpreter.py` — AST evaluation and execution.
- `src/lexer.py` — lexical analysis.
- `src/parser.py` — syntax analysis and AST construction.
- `src/runtime_errors.py` — runtime error definitions.
- `src/token_types.py` — token definitions.
- `tests/` — sample SINS programs.
- `run_parser.py` — program entry point.
- `docs/` — project documentation.

## How to Run

Run these commands from the `part4-interpreter` directory:

```bash
python3 run_parser.py tests/01_arithmetic.sins
python3 run_parser.py tests/02_variables.sins
python3 run_parser.py tests/03_comparisons.sins
python3 run_parser.py tests/04_if_else.sins
python3 run_parser.py tests/05_while.sins
```

The interpreter prints program output to standard output. Lexical, syntax, and runtime errors are reported to standard output with a nonzero exit status.

## Grammar

The following EBNF describes the core syntax supported by the assignment.

```ebnf
program       = { statement } ;
statement     = declaration
              | assignment
              | print_stmt
              | if_stmt
              | while_stmt
              | block ;

declaration   = "let", identifier, "=", expression, ";" ;
assignment    = identifier, "=", expression, ";" ;
print_stmt    = "print", "(", expression, ")", ";" ;
if_stmt       = "if", "(", expression, ")", statement,
                [ "else", statement ] ;
while_stmt    = "while", "(", expression, ")", statement ;
block         = "{", { statement }, "}" ;

expression    = comparison ;
comparison    = addition, [ comparison_op, addition ] ;
comparison_op = "==" | "!=" | "<" | ">" | "<=" | ">=" ;
addition      = multiplication, { ("+" | "-"), multiplication } ;
multiplication = factor, { ("*" | "/"), factor } ;
factor        = number | identifier | "(", expression, ")" ;
```

## Test Programs and Results

The following outputs are expected results for the five sample programs. Actual results must be confirmed by running the programs.

| Test program | Expected output |
|---|---|
| `arithmetic.sins` | `14`, `20` |
| `variable.sins` | `15`, `11` |
| `comparisons.sins` | `True` six times |
| `if_else.sins` | `12` |
| `while.sins` | `1`, `2`, `3`, `4`, `5`, each on a separate line |

### Runtime Error Checks

Additional error cases should include reading an undefined variable and dividing by zero. The interpreter should report a runtime error instead of silently returning an incorrect result.

### Actual Results

arithmetic.sins:
14 
20

variable.sins:
15
11

comparisons.sins:
True
True
True
True
True
True

if_else.sins:
12

while.sins:
1
2
3
4
5


## AI Use Statement

AI assistance was used to help review the interpreter design, AST node structure, parser precedence, variable environment, and test cases. Suggestions were checked against the existing project files and adapted to the project's token names, imports, and runtime error classes. The team should document which suggestions it verified, modified, or rejected and independently verify the resulting implementation before submission.

## Limitations

The listed test outputs are expected results until execution confirms them. Any unsupported language features or remaining errors should be documented based on actual testing.
