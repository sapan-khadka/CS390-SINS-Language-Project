# SINS Parser and Abstract Syntax Tree

This folder contains Part 3 of the SINS language project. The parser converts tokens from the updated lexer into an Abstract Syntax Tree (AST).

## Requirements

- Python 3.10 or later
- No external packages required

## Features

- Numbers and variables
- Arithmetic expressions
- Parenthesized expressions
- Correct operator precedence
- Variable declarations and assignments
- Print statements
- Multiple statements
- Meaningful syntax errors with source locations

## Project Structure

```text
part3-parser/
├── src/
│   ├── __init__.py
│   ├── token_types.py
│   ├── lexer.py
│   ├── ast_nodes.py
│   └── parser.py
├── tests/
│   └── test_parser.py
├── docs/
│   ├── AST_EXAMPLES.md
│   ├── GRAMMAR.ebnf
│   ├── AI_USE_STATEMENT.md
│   └── README.md
├── run_parser.py
└── README.md
```

## Run the Parser

From the `part3-parser` directory:

```bash
python3 run_parser.py path/to/program.sins
```

Example SINS program:

```sins
let x = 2 + 3 * 4;
print x;
```

## Run the Tests

From the `part3-parser` directory:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

The test suite contains 12 tests covering valid statements, expressions, multiple statements, and syntax errors.

## Documentation

- `docs/GRAMMAR.ebnf` contains the updated parser grammar.
- `docs/AST_EXAMPLES.md` contains AST output for three programs.
- `docs/AI_USE_STATEMENT.md` documents the group's use and verification of AI assistance.
