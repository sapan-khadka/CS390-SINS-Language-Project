# Part 6: Lexer, Parser, AST, and Grammar

## 1. Lexer

The SINS lexer converts source code into tokens that can be processed by the parser. It recognizes keywords such as let, print, if, else, while, func, and return. It also recognizes identifiers, integer and decimal numbers, strings, arithmetic operators, comparison operators, and punctuation.

The lexer tracks line and column positions to help identify lexical errors. It supports escaped characters in strings, including newline, tab, quote, and backslash. It appends an end-of-file token after processing the source code.

## 2. Parser

The SINS parser reads the tokens produced by the lexer and checks whether the program follows the language grammar. It supports variable declarations, assignments, print statements, blocks, conditionals, loops, function definitions, function calls, and return statements.

Expressions are parsed using separate precedence levels. Multiplication and division have higher precedence than addition and subtraction. Comparison expressions are handled at a separate level. Parentheses allow programmers to control evaluation order.

For example, 2 + 3 * 4 is interpreted as 2 + (3 * 4), producing 14.

## 3. Abstract Syntax Tree (AST)

The Abstract Syntax Tree represents the logical structure of a program after parsing. It removes the need to preserve the original whitespace and formatting of the source code.

The implementation includes nodes for programs, numbers, strings, variables, binary operations, assignments, print statements, blocks, if statements, while loops, function definitions, function calls, and return statements.

For the expression 2 + 3 * 4, the AST has addition as its root operation. The left child represents 2, while the right child represents the multiplication of 3 and 4. This structure preserves operator precedence.

## 4. EBNF Grammar

The SINS EBNF grammar describes the valid structure of programs. It defines statements such as variable declarations, assignments, print statements, conditionals, loops, function definitions, returns, blocks, and expressions.

Expressions are divided into precedence levels:

- Comparison: equality and relational operators.
- Addition: addition and subtraction.
- Multiplication: multiplication and division.
- Factor: numbers, strings, variables, function calls, and parenthesized expressions.

This layered grammar makes operator precedence clear and helps the parser construct the correct AST.

## 5. Review Notes

The lexer permits identifiers beginning with an underscore, so the EBNF identifier rule should also permit an underscore as the first character.

The grammar should also be checked against the parser's expression-statement behavior. The current parser accepts fewer expression-statement starting forms than the general expression-statement rule in the grammar suggests.
