# SINS Programming Language — Final Project Report

## Group Members

- Sapan Khadka
- Swopnil Dahal
- Nathaniel Kirkpatrick
- Ian Hemingway

## 1. Language Purpose and Overview
SINS is a small interpreted programming language created to demonstrate the major stages of language processing. Its name represents the initials of the four group members: Sapan, Ian, Nathaniel, and Swopnil. The language uses a readable syntax intended for beginner-level programs while still supporting essential programming concepts.

SINS supports variables, assignments, arithmetic expressions, operator precedence, comparisons, print statements, conditional statements, loops, functions, parameters, return values, and global and local scope. Strings were selected as the extension feature. The completed interpreter processes a source program through the following pipeline: source code, lexical analysis, tokens, parsing, abstract syntax tree construction, interpretation, and program output.
## 2. Language Design Decisions
The group designed SINS with a small collection of familiar keywords, including `let`, `print`, `if`, `else`, `while`, `func`, and `return`. Statements generally end with semicolons, while braces define blocks and function bodies. These choices make the language familiar to students who have experience with languages such as Java, JavaScript, C++, or Python.

Arithmetic operators follow standard mathematical precedence. Multiplication and division are evaluated before addition and subtraction, while parentheses can explicitly control evaluation order. Comparison operators produce Boolean values that can be used by conditional statements and loops.

Variables are declared with the `let` keyword. Functions can accept parameters, create local variables, and return values. The environment uses nested scopes so local declarations do not incorrectly replace unrelated global variables. Strings were added as the extension because they make programs more expressive and allow meaningful text output, escape sequences, and concatenation.
## 3. BNF/EBNF Grammar
The SINS EBNF grammar describes the valid structure of programs. It defines statements such as variable declarations, assignments, print statements, conditionals, loops, function definitions, returns, blocks, and expressions.

Expressions are divided into precedence levels:

- Comparison: equality and relational operators.
- Addition: addition and subtraction.
- Multiplication: multiplication and division.
- Factor: numbers, strings, variables, function calls, and parenthesized expressions.

This layered grammar makes operator precedence clear and helps the parser construct the correct AST.

## 4. Lexer Design
The SINS lexer converts source code into tokens that can be processed by the parser. It recognizes keywords such as let, print, if, else, while, func, and return. It also recognizes identifiers, integer and decimal numbers, strings, arithmetic operators, comparison operators, and punctuation.

The lexer tracks line and column positions to help identify lexical errors. It supports escaped characters in strings, including newline, tab, quote, and backslash. It appends an end-of-file token after processing the source code.

## 5. Parser Design
The SINS parser reads the tokens produced by the lexer and checks whether the program follows the language grammar. It supports variable declarations, assignments, print statements, blocks, conditionals, loops, function definitions, function calls, and return statements.

Expressions are parsed using separate precedence levels. Multiplication and division have higher precedence than addition and subtraction. Comparison expressions are handled at a separate level. Parentheses allow programmers to control evaluation order.

For example, 2 + 3 * 4 is interpreted as 2 + (3 * 4), producing 14.

## 6. AST Structure
The Abstract Syntax Tree represents the logical structure of a program after parsing. It removes the need to preserve the original whitespace and formatting of the source code.

The implementation includes nodes for programs, numbers, strings, variables, binary operations, assignments, print statements, blocks, if statements, while loops, function definitions, function calls, and return statements.

For the expression 2 + 3 * 4, the AST has addition as its root operation. The left child represents 2, while the right child represents the multiplication of 3 and 4. This structure preserves operator precedence.

## 7. Interpreter Implementation
[Nathaniel's section]

## 8. Environment and Symbol Table
[Nathaniel's section]

## 9. Functions and Scope
In SINS, you can create a function in order to isolate segments of code into neat, compact packages. These functions can also have input arguments to allow for complex interactions, such as creating mathematical algorithms with input numbers. However, said input arguments are not required, and a function can simply be an isolated block of code that can be called multiple times. Variables declared in functions do not directly interact with variables declared outside of functions, even if said variables have the same name. However, variables from outside of functions can be directly manipulated inside of said functions as long as the code to reference said outside variable comes before a local declaration shadows it.

## 10. String Extension
In SINS, strings are created by surrounding lines of text, numbers, or symbols in single-quotes, 'like this'. Setting a variable to a string is as easy as declaring any other variable. Strings have several escape sequences which allow for otherwise-unusable characters and formatting.

`\'` allows you to add a single-quote to the string without terminating said string.

`\\` allows you to add a backslash into the string.

`\n` creates a new line in the string, allowing for multi-line strings.

`\t` adds a large space to the string, similar to pressing tab in some text editors.

Strings can also be concatenated via the `+` operator. You can do this via adding string variables together as if they were numbers, or you can concatenate strings together in a `print` statement. You can also add the value of other types of variables to strings this way as well, and it will concatenate the values to the string as if they themselves were strings.

## 11. Error Handling
[Nathaniel's section]

## 12. Testing Strategy
The testing strategy combines automated unit tests with complete SINS source programs. Unit tests verify individual components such as the environment, scope behavior, parser, and function syntax. Complete programs verify that the entire pipeline works correctly from source code through final output.

The final suite contains programs covering arithmetic, operator precedence, variables, assignments, print statements, comparisons, conditional statements, loops, functions, scope, and strings. Additional programs intentionally contain an invalid character, invalid syntax, an undefined variable, and division by zero. These error programs confirm that failures are detected and reported instead of causing unexplained interpreter crashes.

Before submission, the group will run the full automated test suite and every complete test program. The observed outputs and error messages will be compared with the expected results. The final README will document the commands required to reproduce these tests.
## 13. Major Challenges
One major challenge was integrating work completed by multiple members on separate branches. Several members modified related files, including the parser, AST nodes, and interpreter. This created merge conflicts that had to be resolved carefully so that newer function and scope behavior was preserved while the string extension was added.

Another challenge involved maintaining consistent names across the lexer, token definitions, parser, and interpreter. A token or AST node name used by one component had to match every other component exactly. The group also encountered a Python import conflict because a project file named `token.py` could shadow Python's standard-library module. Testing from the correct project directory helped identify and avoid that issue.

Scope handling was also challenging because function-local variables needed access to appropriate outer values without leaking into the global environment. The group addressed this by using linked environments and testing shadowing, local declarations, parameter binding, and assignment behavior.
## 14. Lessons Learned
The project demonstrated that a programming language is a collection of closely connected components rather than a single program. A correct lexer is not sufficient if the parser expects different token names, and a correct parser is not sufficient if the interpreter does not support the generated AST nodes.

The group learned the importance of defining interfaces early, using consistent naming, testing after every integration, and keeping individual work in separate Git branches. Pull requests and visible commits made it possible to review contributions and preserve authorship.

The group also learned that automated assistance must be verified against the actual implementation. Suggested code can look correct while using incompatible names, assumptions, or file structures. Reading the code, running tests, reviewing outputs, and correcting integration problems remained the responsibility of the group.
## 15. Individual Contributions
**Sapan Khadka:** Coordinated the group, managed the GitHub repository and integration branches, implemented and reviewed scope-related project structure, resolved integration conflicts, organized the final test suite, assembled the report and documentation, prepared the final submission, and coordinated the recorded demonstration.

**Swopnil Dahal:** Developed function-related AST and parser support, added parser tests, and contributed to expression and function parsing. For Part 6, Swopnil reviewed the lexer, parser, AST, and grammar and prepared basic-language test programs and corresponding report sections.

**Nathaniel Kirkpatrick:** Implemented function execution and runtime behavior in the interpreter. For Part 6, Nathaniel reviewed interpreter execution, control flow, the environment, and error handling and prepared control-flow and intentional-error test programs.

**Ian Hemingway:** Implemented the strings extension, including string parsing, evaluation, escape sequences, and concatenation. For Part 6, Ian reviewed functions, scope, strings, and associated runtime errors and prepared the relevant test programs and report sections.

All members reviewed the overall architecture and participated in testing, documentation, GitHub collaboration, and the recorded demonstration.
## 16. Generative AI Use
The group used ChatGPT as a development assistant for requirement clarification, task organization, Git and GitHub guidance, test planning, debugging suggestions, documentation structure, and explanations of lexer, parser, AST, interpreter, function, and scope concepts. AI assistance did not replace the group's responsibility for implementing, understanding, testing, and presenting the project.

One AI-generated suggestion used token names that did not match the project's existing `TokenType` definitions. The suggestion referred to names such as `LESS` and `GREATER`, while the project used `LESS_THAN` and `GREATER_THAN`. The mismatch produced an error and required correction. Other AI-assisted integration suggestions also required adjustment to preserve the existing function and nested-scope implementation while adding strings.

The group verified AI-assisted work by reviewing the generated changes, compiling the Python files, running automated unit tests, executing complete SINS programs, checking expected output, and testing intentional lexical, syntax, and runtime failures. Each member remained responsible for understanding and explaining the submitted implementation.
## GitHub Repository

https://github.com/sapan-khadka/CS390-SINS-Language-Project
