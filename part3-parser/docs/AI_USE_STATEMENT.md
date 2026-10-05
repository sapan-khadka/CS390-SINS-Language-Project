# AI USE STATEMENT

## AI Tool(s) Used

ChatGPT

## How did your group use AI for this project milestone?

Our group used ChatGPT to clarify the Part 3 requirements, divide responsibilities, plan the repository structure, check compatibility between the existing lexer and parser, troubleshoot Git and Python import-path issues, plan tests, and organize documentation. Group members remained responsible for implementing, reviewing, testing, and understanding the submitted work.

## Which project components received AI assistance?

AI assistance was used for repository organization, lexer-to-parser integration planning, command-line runner guidance, test planning, error-handling review, documentation organization, and this AI Use Statement. The group reviewed and tested the parser, AST implementation, grammar, tests, and generated outputs before submission.

## Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.

An initial AI-assisted organization plan assumed that parser files could be added before checking compatibility with the existing repository. The group found that the parser expected imports from the `src` package, so placing files elsewhere would cause import errors. We corrected the structure by placing the lexer, parser, AST nodes, and token definitions inside `part3-parser/src/`. We also corrected the test command: running `python3 tests/test_parser.py` caused `ModuleNotFoundError: No module named 'src'`, while running unittest discovery from the project directory correctly located the package.

## How did your group test or independently verify AI-assisted work?

We ran 12 automated parser tests using `python3 -m unittest discover -s tests -p "test_*.py" -v`, and all tests passed. The tests covered variable declarations, assignments, print statements, multiple statements, arithmetic expressions, parenthesized expressions, and invalid syntax. We also ran the command-line parser on three programs and inspected their AST output to verify multiplication and division precedence and the effect of parentheses.

## What did your group learn from using AI during this milestone?

We learned that AI suggestions must be checked against the project's existing interfaces, grammar, package structure, and team responsibilities. Correct-looking code can still fail because of incompatible imports or execution commands. Incremental testing, reviewing pull requests, and comparing AST output with the expected structure helped the group identify and correct these issues.
