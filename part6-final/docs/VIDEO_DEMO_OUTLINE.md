# SINS Final Demonstration Outline

Target length: 10–15 minutes

## 1. Introduction — Sapan — 1 minute

- Introduce Sapan Khadka, Swopnil Dahal, Nathaniel Kirkpatrick, and Ian Hemingway.
- Explain that SINS is a small interpreted programming language.
- State that strings are the selected extension feature.
- Summarize the major supported features.

## 2. System Architecture — Sapan — 1 minute

Explain the pipeline:

Source Program → Lexer → Tokens → Parser → AST → Interpreter → Output

Briefly explain the purpose of each stage.

## 3. Lexer Demonstration — Swopnil — 1.5 minutes

- Open a SINS program.
- Run the lexer and display its tokens.
- Identify keywords, identifiers, numbers, strings, operators, and delimiters.
- Explain lexical error detection.

## 4. Parser and AST — Swopnil — 1.5 minutes

- Demonstrate `2 + 3 * 4`.
- Display or describe the generated AST.
- Explain why multiplication is evaluated before addition.
- Show an important portion of `parser.py` and `ast_nodes.py`.

## 5. Interpreter and Control Flow — Nathaniel — 2 minutes

- Demonstrate variables and assignments.
- Demonstrate print and comparisons.
- Run an `if/else` program.
- Run a `while` loop.
- Show an important portion of `interpreter.py`.

## 6. Functions and Scope — Ian — 2 minutes

- Demonstrate a function with parameters.
- Demonstrate a return value.
- Demonstrate global and local variables.
- Explain parameter binding and nested environments.
- Show the relevant function and environment code.

## 7. Strings Extension — Ian — 1 minute

- Demonstrate string literals.
- Demonstrate escape sequences.
- Demonstrate string concatenation.
- Explain how strings were added to the lexer, parser, AST, and interpreter.

## 8. Error Handling — Nathaniel — 1.5 minutes

Demonstrate at least two:

- Invalid character
- Invalid syntax
- Undefined variable
- Division by zero

Explain which stage detects each error.

## 9. Testing and GitHub — Sapan — 1 minute

- Show the final test-program directory.
- Run the automated tests.
- Explain that complete programs cover all required features.
- Briefly show the group’s individual GitHub contributions.

## 10. Generative AI Use — Sapan — 1 minute

- State that ChatGPT assisted with planning, debugging, Git guidance, testing, and documentation.
- Explain the incorrect token-name suggestion that required correction.
- Explain how the group verified AI-assisted work through review and testing.

## 11. Conclusion — Sapan — 30 seconds

- Confirm that the final interpreter supports all required features.
- Thank the audience.
- Display the GitHub repository link.

## Recording Checklist

- Every member identifies themselves.
- Every member speaks and demonstrates their assigned component.
- Avoid simply scrolling through code.
- Show important methods only.
- Keep the terminal text large and readable.
- Remove personal information and unrelated browser tabs.
- Record clear audio.
- Keep the video between 10 and 15 minutes.
- Upload the video as Unlisted if using YouTube.
- Test the final link in a private/incognito window.
