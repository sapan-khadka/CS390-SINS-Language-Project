# SINS Parser and Abstract Syntax Tree

This folder contains Part 3 of the SINS language project. The parser converts tokens from the updated SINS lexer into an Abstract Syntax Tree (AST).

## Requirements

- Python 3.10 or later
- No external Python packages are required

## Planned Project Structure

```text
part3-parser/
├── src/
│   ├── __init__.py
│   ├── token_types.py
│   ├── lexer.py
│   ├── ast_nodes.py
│   └── parser.py
├── tests/
│   ├── test_parser.py
│   ├── test_inputs/
│   └── ast_outputs/
├── docs/
│   ├── EBNF.md
│   └── AI_USE_STATEMENT.md
├── run_parser.py
└── README.md
```

## Integration Contract

- The lexer is called with `Lexer(source).tokenize()`.
- The parser should be called with `Parser(tokens).parse()`.
- Parsing returns a `ProgramNode`.
- Lexical and syntax errors must display meaningful messages with source locations.
- AST nodes must have readable string representations so outputs can be saved and reviewed.

## Team Workflow

Each member works on an individual branch, adds tests for assigned work, opens a pull request into `main`, and receives a review before merging.

Detailed running and testing instructions will be completed after the parser and AST modules are integrated.
