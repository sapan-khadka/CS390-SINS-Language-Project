# SINS Lexical Analyzer

This project implements a lexical analyzer for the SINS programming language designed in Part 1.

The lexer reads SINS source code and converts it into a sequence of tokens representing keywords, identifiers, numbers, strings, operators, and delimiters.

## Requirements

- Python 3.10 or later
- No external Python packages are required

## Project Structure

```text
part2-lexer/
├── src/
│   ├── __init__.py
│   ├── token_types.py
│   └── lexer.py
├── tests/
│   ├── test_inputs/
│   └── expected_outputs/
├── docs/
├── run_lexer.py
└── README.md
