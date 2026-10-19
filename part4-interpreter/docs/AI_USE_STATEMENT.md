# AI USE STATEMENT

## AI Tool(s) Used

ChatGPT

## How did your group use AI for this project milestone?

Our group used ChatGPT to clarify project requirements, plan lexer and parser changes, reason about arithmetic operator precedence and comparison operators, troubleshoot Python and test issues, and organize the interpreter's documentation. Group members remained responsible for implementing, reviewing, testing, and understanding the submitted work.

## Which project components received AI assistance?

AI assistance was used for planning and reviewing lexer and parser functionality, AST node design, grammar updates, test planning, runtime error handling, command-line execution guidance, and documentation. The group reviewed the implementation and checked program outputs and automated test results.

## Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.

During testing, an existing parser test expected the error message `Expected a value after '='`, but the parser produced a different message when a declaration or assignment was missing its value. With AI-assisted troubleshooting, we identified the mismatch and updated the relevant parser error messages to match the test's expected wording. We then reran the automated test suite to verify the change. This correction changed the error-message text rather than the language's parsing behavior.

## How did your group test or independently verify AI-assisted work?

We ran the automated test suite from the `part4-interpreter` directory using `python -m pytest`. The suite passed all 19 tests. We also ran interpreter programs to check arithmetic precedence and parentheses, comparison operators, conditional execution, and while-loop behavior. For example, arithmetic tests produced `14` for `2 + 3 * 4` and `20` for `(2 + 3) * 4`. Comparison tests produced the expected `True` results, and the while-loop example printed the sequence from 1 through 5.

We compared observed outputs with expected results to help verify the interpreter's behavior.

## What did your group learn from using AI during this milestone?

We learned that AI suggestions must be checked against the actual codebase, existing interfaces, grammar, and tests. An explanation or code suggestion can be useful but may need modification to fit the project's implementation and test expectations. Running tests, inspecting program output, and reviewing changes helped us identify issues and verify corrections. The group remains responsible for the correctness and understanding of the submitted project.

