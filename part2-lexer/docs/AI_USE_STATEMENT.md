# AI USE STATEMENT

## AI Tool(s) Used

ChatGPT

## How did your group use AI for this project milestone?

Our group used ChatGPT to help interpret the project requirements, organize the repository, plan the division of responsibilities, suggest parts of the Python lexer structure, troubleshoot errors, develop test ideas, and improve the README and other documentation. Group members reviewed the suggestions before including them in the project.

## Which project components received AI assistance?

AI assistance was used for repository organization, token-definition planning, the command-line runner, portions of lexer integration and debugging, test-case planning, documentation, and the AI Use Statement. The final source code and documentation were reviewed, tested, and corrected by the group.

## Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.

An AI-generated lexer suggestion used the token names `LESS` and `GREATER`. Our token definitions actually used `LESS_THAN` and `GREATER_THAN`. This mismatch caused an `AttributeError` during testing. We corrected the lexer to use the token names defined in `token_types.py` and reran the tests successfully.

## How did your group test or independently verify AI-assisted work?

We ran eight lexer test cases covering variable declarations, arithmetic expressions, print statements, control structures, functions, invalid characters, the `end` statement, and decimal numbers. We also tested the command-line runner using a `.sins` source file. The group compared the produced tokens with the expected outputs and confirmed that invalid characters generated meaningful lexical errors.

## What did your group learn from using AI during this milestone?

We learned that AI suggestions must be checked against the project’s existing token definitions, grammar, and file structure. Even when suggested code appears reasonable, naming differences can cause runtime errors. Running tests and reviewing the output helped us identify and correct these inconsistencies.

