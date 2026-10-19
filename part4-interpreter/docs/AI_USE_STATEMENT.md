# AI USE STATEMENT

## AI Tool(s) Used

ChatGPT

## How did your group use AI for this project milestone?

Our group used ChatGPT to help clarify the Part 4 requirements, divide responsibilities, organize the interpreter project structure, plan the environment and runtime-error classes, troubleshoot lexer-parser-interpreter integration problems, develop testing commands, review documentation, and prepare the final submission structure. Group members remained responsible for implementing, reviewing, testing, correcting, and understanding the submitted work.

## Which project components received AI assistance?

AI assistance was used for planning the environment/symbol table, runtime-error handling, command-line interpreter runner, integration workflow, test planning, grammar review, README organization, and this AI Use Statement. AI was also used to help diagnose errors encountered while combining the lexer, parser, AST nodes, and interpreter.

## Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.

During integration, an AI-assisted lexer edit contained an incorrectly indented EOF-token block and a mismatched closing brace. This produced an `IndentationError` and then a `SyntaxError`. The group inspected the affected lines and corrected the block so that the EOF token was appended correctly before returning the token list. We also corrected a parser error message so it matched the expected test behavior. After making these changes, we reran the complete test suite successfully.

## How did your group test or independently verify AI-assisted work?

We ran 19 automated tests using:

`python3 -m unittest discover -s tests -p "test_*.py" -v`

All 19 tests passed. We also executed five complete SINS programs covering arithmetic, variables, comparisons, `if/else`, and `while` loops. Their actual outputs matched the expected outputs. Additional manual tests confirmed correct handling of undefined variables and division by zero.

## What did your group learn from using AI during this milestone?

We learned that AI-generated suggestions must be checked against the existing token definitions, AST node interfaces, parser behavior, project structure, and assignment requirements. Code that appears correct can still contain indentation, syntax, naming, or integration errors. Running automated tests and complete programs after every integration change was necessary to verify and correct the work.
