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
[Swopnil's section]

## 4. Lexer Design
[Swopnil's section]

## 5. Parser Design
[Swopnil's section]

## 6. AST Structure
[Swopnil's section]

## 7. Interpreter Implementation
[Nathaniel's section]

## 8. Environment and Symbol Table
[Nathaniel's section]

## 9. Functions and Scope
[Ian's section]

## 10. String Extension
[Ian's section]

## 11. Error Handling
[Nathaniel's section]

## 12. Testing Strategy

## 13. Major Challenges

## 14. Lessons Learned

## 15. Individual Contributions

## 16. Generative AI Use

## GitHub Repository

https://github.com/sapan-khadka/CS390-SINS-Language-Project
