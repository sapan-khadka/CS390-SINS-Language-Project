# AI Use Statement

Our group used ChatGPT to help clarify the project requirements, organize the Part 2 repository structure, review token definitions, suggest test cases, and troubleshoot errors. We reviewed and tested all AI-assisted suggestions before including them in the project.

One AI-generated suggestion that we corrected involved comparison-token names. The suggested lexer initially used `LESS` and `GREATER`, but our `TokenType` definition used `LESS_THAN` and `GREATER_THAN`. Running the test suite produced an `AttributeError`, which allowed us to identify the mismatch. We corrected the lexer to use the token names defined by our project and ran all seven tests again. The corrected lexer successfully recognized valid input and produced a meaningful error for the invalid `@` character.

AI assistance supported our development process, but the group remained responsible for reviewing, testing, correcting, and understanding the submitted code.

