# AI USE STATEMENT

## AI Tool(s) Used

ChatGPT

## How did your group use AI for this project milestone?

Our group used ChatGPT to clarify the Part 3 requirements, divide responsibilities, plan the repository structure, check compatibility between the existing lexer and the parser, troubleshoot Git and import-path issues, and prepare a command-line runner. AI was used as a development aid, while group members remained responsible for implementing, reviewing, testing, and understanding the submitted work.

## Which project components received AI assistance?

AI assistance was used for the Part 3 folder organization, the lexer-to-parser integration plan, the command-line runner, test-planning guidance, error-handling review, documentation organization, and this AI Use Statement. The parser logic, AST implementation, grammar, tests, and outputs are assigned to group members and will be reviewed before submission.

## Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.

An initial AI-assisted organization plan assumed that new parser files could be placed directly into the repository before reviewing the existing branches. The group checked Nathaniel's branch and found that its parser imported `src.lexer` and `.token_types` even though the files were stored at the repository root. That structure would cause import errors. We corrected the integration plan by creating a proper `part3-parser/src/` Python package, retaining the verified Part 2 lexer interface, and requiring parser and AST files to be placed inside that package. We also preserved the team member's contribution instead of duplicating or replacing it.

## How did your group test or independently verify AI-assisted work?

We pulled the integration branch onto a local Mac, confirmed the expected project files, and ran the updated lexer on `let x = 2 + 3 * 4;`. The lexer produced the expected tokens in the correct order. We then used Python's `py_compile` module to verify that the lexer, token definitions, and command-line parser runner contained valid Python syntax. After the parser and AST modules are integrated, the group will run the full parser test suite, verify operator precedence, compare at least three AST outputs, and confirm meaningful syntax errors.

## What did your group learn from using AI during this milestone?

We learned that AI suggestions must be checked against the project's existing interfaces, repository structure, grammar, and team responsibilities. Correct-looking code may still fail when files are stored in the wrong package or use incompatible imports. Reviewing branches, testing incrementally, and preserving clear ownership helped the group identify these issues before final integration.
