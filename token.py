
# SINS token types

LET = "LET"
PRINT = "PRINT"
IF = "IF"
ELSE = "ELSE"
WHILE = "WHILE"
FUNC = "FUNC"
RETURN = "RETURN"
END = "END"

IDENTIFIER = "IDENTIFIER"
NUMBER = "NUMBER"
STRING = "STRING"

ASSIGN = "ASSIGN"

PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"

EQUAL = "EQUAL"
NOT_EQUAL = "NOT_EQUAL"
LESS = "LESS"
LESS_EQUAL = "LESS_EQUAL"
GREATER = "GREATER"
GREATER_EQUAL = "GREATER_EQUAL"

LPAREN = "LPAREN"
RPAREN = "RPAREN"
LBRACE = "LBRACE"
RBRACE = "RBRACE"
SEMICOLON = "SEMICOLON"
COMMA = "COMMA"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.type}({self.value})"
        return self.type