"""Token definitions for the SINS programming language."""

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    # Keywords
    LET = auto()
    PRINT = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FUNC = auto()
    RETURN = auto()
    END = auto()

    # Values
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    # Arithmetic operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    # Assignment and comparison operators
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS_THAN = auto()
    LESS_EQUAL = auto()
    GREATER_THAN = auto()
    GREATER_EQUAL = auto()

    # Delimiters
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    SEMICOLON = auto()

    # End of input
    EOF = auto()


@dataclass(frozen=True)
class Token:
    token_type: TokenType
    lexeme: str
    line: int
    column: int

    def __str__(self) -> str:
        value_tokens = {
            TokenType.IDENTIFIER,
            TokenType.NUMBER,
            TokenType.STRING,
        }

        if self.token_type in value_tokens:
            return f"{self.token_type.name}({self.lexeme})"

        return self.token_type.name


KEYWORDS = {
    "let": TokenType.LET,
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
    "func": TokenType.FUNC,
    "return": TokenType.RETURN,
    "end": TokenType.END,
}
