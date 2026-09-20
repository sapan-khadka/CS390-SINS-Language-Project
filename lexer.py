from token import (
    Token,
    LET, PRINT, IF, ELSE, WHILE, FUNC, RETURN, END,
    IDENTIFIER, NUMBER, STRING,
    ASSIGN,
    PLUS, MINUS, MULTIPLY, DIVIDE,
    EQUAL, NOT_EQUAL, LESS, LESS_EQUAL, GREATER, GREATER_EQUAL,
    LPAREN, RPAREN, LBRACE, RBRACE, SEMICOLON, COMMA
)


KEYWORDS = {
    "let": LET,
    "print": PRINT,
    "if": IF,
    "else": ELSE,
    "while": WHILE,
    "func": FUNC,
    "return": RETURN,
    "end": END
}


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0

    def tokenize(self):
        tokens = []

        while self.position < len(self.source):
            current = self.source[self.position]

            # Ignore whitespace
            if current.isspace():
                self.position += 1
                continue

            # Identifiers and keywords
            if current.isalpha() or current == "_":
                tokens.append(self.read_identifier())
                continue

            # Numbers
            if current.isdigit():
                tokens.append(self.read_number())
                continue

            # Strings
            if current == "'":
                tokens.append(self.read_string())
                continue

            # Two-character operators
            two_char = self.source[self.position:self.position + 2]

            if two_char == "==":
                tokens.append(Token(EQUAL))
                self.position += 2
                continue

            if two_char == "!=":
                tokens.append(Token(NOT_EQUAL))
                self.position += 2
                continue

            if two_char == "<=":
                tokens.append(Token(LESS_EQUAL))
                self.position += 2
                continue

            if two_char == ">=":
                tokens.append(Token(GREATER_EQUAL))
                self.position += 2
                continue

            # One-character operators and delimiters
            single_char_tokens = {
                "=": ASSIGN,
                "+": PLUS,
                "-": MINUS,
                "*": MULTIPLY,
                "/": DIVIDE,
                "<": LESS,
                ">": GREATER,
                "(": LPAREN,
                ")": RPAREN,
                "{": LBRACE,
                "}": RBRACE,
                ";": SEMICOLON,
                ",": COMMA
            }

            if current in single_char_tokens:
                tokens.append(Token(single_char_tokens[current]))
                self.position += 1
                continue

            # Unknown character
            raise LexerError(
                f"Invalid character '{current}' at position {self.position}"
            )

        return tokens

    def read_identifier(self):
        start = self.position

        while (
            self.position < len(self.source)
            and (
                self.source[self.position].isalnum()
                or self.source[self.position] == "_"
            )
        ):
            self.position += 1

        value = self.source[start:self.position]

        if value in KEYWORDS:
            return Token(KEYWORDS[value])

        return Token(IDENTIFIER, value)

    def read_number(self):
        start = self.position
        decimal_found = False

        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isdigit():
                self.position += 1

            elif current == "." and not decimal_found:
                decimal_found = True
                self.position += 1

            else:
                break

        value = self.source[start:self.position]
        return Token(NUMBER, value)

    def read_string(self):
        # Skip opening quote
        self.position += 1
        start = self.position

        while self.position < len(self.source):
            if self.source[self.position] == "'":
                value = self.source[start:self.position]
                self.position += 1
                return Token(STRING, value)

            self.position += 1

        raise LexerError("Unterminated string")