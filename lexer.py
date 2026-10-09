"""Lexer for the SINS programming language."""

from token_types import Token, TokenType, KEYWORDS


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def advance(self):
        current = self.source[self.position]
        self.position += 1

        if current == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

    def tokenize(self):
        tokens = []

        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isspace():
                self.advance()
                continue

            start_line = self.line
            start_column = self.column

            if current.isalpha() or current == "_":
                tokens.append(
                    self.read_identifier(start_line, start_column)
                )
                continue

            if current.isdigit():
                tokens.append(
                    self.read_number(start_line, start_column)
                )
                continue

            if current == "'":
                tokens.append(
                    self.read_string(start_line, start_column)
                )
                continue

            two_char = self.source[self.position:self.position + 2]

            two_char_tokens = {
                "==": TokenType.EQUAL,
                "!=": TokenType.NOT_EQUAL,
                "<=": TokenType.LESS_EQUAL,
                ">=": TokenType.GREATER_EQUAL,
            }

            if two_char in two_char_tokens:
                self.advance()
                self.advance()

                tokens.append(
                    Token(
                        two_char_tokens[two_char],
                        two_char,
                        start_line,
                        start_column
                    )
                )
                continue

            single_char_tokens = {
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
                ",": TokenType.COMMA,
                ";": TokenType.SEMICOLON,
            }

            if current in single_char_tokens:
                self.advance()

                tokens.append(
                    Token(
                        single_char_tokens[current],
                        current,
                        start_line,
                        start_column
                    )
                )
                continue

            raise LexerError(
                f"Invalid character {current!r} at "
                f"line {start_line}, column {start_column}"
            )

        tokens.append(
            Token(TokenType.EOF, "", self.line, self.column)
        )

        return tokens

    def read_identifier(self, start_line, start_column):
        start = self.position

        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isalnum() or current == "_":
                self.advance()
            else:
                break

        value = self.source[start:self.position]

        if value in KEYWORDS:
            token_type = KEYWORDS[value]
        else:
            token_type = TokenType.IDENTIFIER

        return Token(
            token_type,
            value,
            start_line,
            start_column
        )

    def read_number(self, start_line, start_column):
        start = self.position
        decimal_found = False

        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isdigit():
                self.advance()
            elif current == "." and not decimal_found:
                decimal_found = True
                self.advance()
            else:
                break

        value = self.source[start:self.position]

        return Token(
            TokenType.NUMBER,
            value,
            start_line,
            start_column
        )

    def read_string(self, start_line, start_column):
        self.advance()
        start = self.position

        while self.position < len(self.source):
            current = self.source[self.position]

            if current == "'":
                value = self.source[start:self.position]
                self.advance()

                return Token(
                    TokenType.STRING,
                    value,
                    start_line,
                    start_column
                )

            if current == "\n":
                raise LexerError(
                    f"Unterminated string starting at "
                    f"line {start_line}, column {start_column}"
                )

            self.advance()

        raise LexerError(
            f"Unterminated string starting at "
            f"line {start_line}, column {start_column}"
        )
