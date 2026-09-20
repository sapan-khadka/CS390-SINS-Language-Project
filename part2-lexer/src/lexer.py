"""Lexical analyzer for the SINS programming language."""

from .token_types import KEYWORDS, Token, TokenType


class LexerError(Exception):
    """Raised when the lexer finds invalid input."""


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self):
        """Convert the source code into a list of tokens."""
        tokens = []

        while not self._at_end():
            current = self._current_character()

            # Ignore whitespace
            if current.isspace():
                self._advance()
                continue

            # Keywords and identifiers
            if current.isalpha() or current == "_":
                tokens.append(self._read_identifier())
                continue

            # Integer and decimal numbers
            if current.isdigit():
                tokens.append(self._read_number())
                continue

            # String values
            if current == "'":
                tokens.append(self._read_string())
                continue

            start_line = self.line
            start_column = self.column
            two_characters = self.source[
                self.position:self.position + 2
            ]

            # Two-character comparison operators
            two_character_tokens = {
                "==": TokenType.EQUAL,
                "!=": TokenType.NOT_EQUAL,
                "<=": TokenType.LESS_EQUAL,
                ">=": TokenType.GREATER_EQUAL,
            }

            if two_characters in two_character_tokens:
                self._advance()
                self._advance()

                tokens.append(
                    Token(
                        two_character_tokens[two_characters],
                        two_characters,
                        start_line,
                        start_column,
                    )
                )
                continue

            # One-character operators and delimiters
            one_character_tokens = {
                "=": TokenType.ASSIGN,
                "+": TokenType.PLUS,
                "-": TokenType.MINUS,
                "*": TokenType.MULTIPLY,
                "/": TokenType.DIVIDE,
                "<": TokenType.LESS,
                ">": TokenType.GREATER,
                "(": TokenType.LEFT_PAREN,
                ")": TokenType.RIGHT_PAREN,
                "{": TokenType.LEFT_BRACE,
                "}": TokenType.RIGHT_BRACE,
                ";": TokenType.SEMICOLON,
                ",": TokenType.COMMA,
            }

            if current in one_character_tokens:
                self._advance()

                tokens.append(
                    Token(
                        one_character_tokens[current],
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

    def _read_identifier(self):
        start_position = self.position
        start_line = self.line
        start_column = self.column

        while (
            not self._at_end()
            and (
                self._current_character().isalnum()
                or self._current_character() == "_"
            )
        ):
            self._advance()

        lexeme = self.source[start_position:self.position]
        token_type = KEYWORDS.get(lexeme, TokenType.IDENTIFIER)

        return Token(
            token_type,
            lexeme,
            start_line,
            start_column,
        )

    def _read_number(self):
        start_position = self.position
        start_line = self.line
        start_column = self.column

        while (
            not self._at_end()
            and self._current_character().isdigit()
        ):
            self._advance()

        # A decimal point must be followed by at least one digit.
        if (
            not self._at_end()
            and self._current_character() == "."
            and self._peek_character().isdigit()
        ):
            self._advance()

            while (
                not self._at_end()
                and self._current_character().isdigit()
            ):
                self._advance()

        lexeme = self.source[start_position:self.position]

        return Token(
            TokenType.NUMBER,
            lexeme,
            start_line,
            start_column,
        )

    def _read_string(self):
        start_line = self.line
        start_column = self.column

        # Skip the opening quotation mark.
        self._advance()
        start_position = self.position

        while (
            not self._at_end()
            and self._current_character() != "'"
        ):
            self._advance()

        if self._at_end():
            raise LexerError(
                "Unterminated string "
                f"at line {start_line}, column {start_column}"
            )

        value = self.source[start_position:self.position]

        # Skip the closing quotation mark.
        self._advance()

        return Token(
            TokenType.STRING,
            value,
            start_line,
            start_column,
        )

    def _current_character(self):
        return self.source[self.position]

    def _peek_character(self):
        next_position = self.position + 1

        if next_position >= len(self.source):
            return "\0"

        return self.source[next_position]

    def _advance(self):
        current = self.source[self.position]
        self.position += 1

        if current == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

    def _at_end(self):
        return self.position >= len(self.source)
