"""Lexical analyzer for the SINS programming language."""

from .token_types import KEYWORDS, Token, TokenType


class LexerError(Exception):
    """Raised when the lexer encounters invalid source code."""


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self) -> list[Token]:
        tokens = []

        while not self.is_at_end():
            current = self.current_character()

            if current.isspace():
                self.advance()
                continue

            if current.isalpha() or current == "_":
                tokens.append(self.read_identifier())
                continue

            if current.isdigit():
                tokens.append(self.read_number())
                continue

            if current == "'":
                tokens.append(self.read_string())
                continue

            start_line = self.line
            start_column = self.column
            two_character = self.source[
                self.position:self.position + 2
            ]

            two_character_tokens = {
                "==": TokenType.EQUAL,
                "!=": TokenType.NOT_EQUAL,
                "<=": TokenType.LESS_EQUAL,
                ">=": TokenType.GREATER_EQUAL,
            }

            if two_character in two_character_tokens:
                self.advance()
                self.advance()
                tokens.append(
                    Token(
                        two_character_tokens[two_character],
                        two_character,
                        start_line,
                        start_column,
                    )
                )
                continue

            single_character_tokens = {
                "=": TokenType.ASSIGN,
                "+": TokenType.PLUS,
                "-": TokenType.MINUS,
                "*": TokenType.MULTIPLY,
                "/": TokenType.DIVIDE,
                "<": TokenType.LESS_THAN,
                ">": TokenType.GREATER_THAN,
                "(": TokenType.LEFT_PAREN,
                ")": TokenType.RIGHT_PAREN,
                "{": TokenType.LEFT_BRACE,
                "}": TokenType.RIGHT_BRACE,
                ";": TokenType.SEMICOLON,
                ",": TokenType.COMMA,
            }

            if current in single_character_tokens:
                self.advance()
                tokens.append(
                    Token(
                        single_character_tokens[current],
                        current,
                        start_line,
                        start_column,
                    )
                )
                continue

            raise LexerError(
                f"Invalid character '{current}' "
                f"at line {self.line}, column {self.column}"
            )

        return tokens

    def read_identifier(self) -> Token:
        start_position = self.position
        start_line = self.line
        start_column = self.column

        while (
            not self.is_at_end()
            and (
                self.current_character().isalnum()
                or self.current_character() == "_"
            )
        ):
            self.advance()

        lexeme = self.source[start_position:self.position]
        token_type = KEYWORDS.get(lexeme, TokenType.IDENTIFIER)

        return Token(
            token_type,
            lexeme,
            start_line,
            start_column,
        )

    def read_number(self) -> Token:
        start_position = self.position
        start_line = self.line
        start_column = self.column

        while (
            not self.is_at_end()
            and self.current_character().isdigit()
        ):
            self.advance()

        if (
            not self.is_at_end()
            and self.current_character() == "."
            and self.peek_character().isdigit()
        ):
            self.advance()

            while (
                not self.is_at_end()
                and self.current_character().isdigit()
            ):
                self.advance()

        lexeme = self.source[start_position:self.position]

        return Token(
            TokenType.NUMBER,
            lexeme,
            start_line,
            start_column,
        )

    def read_string(self) -> Token:
        start_line = self.line
        start_column = self.column

        self.advance()
        start_position = self.position

        while (
            not self.is_at_end()
            and self.current_character() != "'"
        ):
            self.advance()

        if self.is_at_end():
            raise LexerError(
                "Unterminated string "
                f"at line {start_line}, column {start_column}"
            )

        lexeme = self.source[start_position:self.position]
        self.advance()

        return Token(
            TokenType.STRING,
            lexeme,
            start_line,
            start_column,
        )

    def current_character(self) -> str:
        return self.source[self.position]

    def peek_character(self) -> str:
        next_position = self.position + 1

        if next_position >= len(self.source):
            return "\0"

        return self.source[next_position]

    def advance(self) -> None:
        current = self.source[self.position]
        self.position += 1

        if current == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

    def is_at_end(self) -> bool:
        return self.position >= len(self.source)
