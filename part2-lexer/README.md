# SINS Lexical Analyzer

This project implements a lexical analyzer for the SINS programming language designed in Part 1.

The lexer reads SINS source code and converts it into tokens representing keywords, identifiers, numbers, strings, operators, and delimiters.

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
```

## Running the Lexer

From inside the `part2-lexer` folder, run:

```bash
python3 run_lexer.py tests/test_inputs/test01_variable.sins
```

The lexer prints one token per line.

## Example

Input:

```sins
let x = 10;
```

Output:

```text
LET
IDENTIFIER(x)
ASSIGN
NUMBER(10)
SEMICOLON
EOF
```

## Error Handling

If the source contains an invalid character, the lexer reports a meaningful lexical error and its location.

## Testing

The tests cover:

- Variable declarations
- Arithmetic expressions
- Print statements
- Control structures
- Invalid input

Additional tests may cover functions, strings, decimals, and the `end` statement.

## Team Workflow

Each group member works on an individual branch and creates a pull request into `main`.
