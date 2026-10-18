from .token_types import TokenType
from .ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    AssignmentNode,
    PrintNode,
)


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        statements = []
        while not self._at_end():
            statements.append(self._parse_statement())
        return ProgramNode(statements)

    def _parse_statement(self):
        if self._match(TokenType.LET):
            return self._parse_declaration()
        if self._match(TokenType.PRINT):
            return self._parse_print()
        if self._check(TokenType.IDENTIFIER):
            return self._parse_assignment()

        token = self._current()
        raise ParserError(
            f"Unexpected token '{token.lexeme}' "
            f"at line {token.line}, column {token.column}"
        )

    def _parse_declaration(self):
        if not self._check(TokenType.IDENTIFIER):
            self._error("Expected a variable name after 'let'")

        name = self._advance().lexeme

        if not self._match(TokenType.ASSIGN):
            self._error(f"Expected '=' after variable name '{name}'")

        if self._check(TokenType.SEMICOLON):
            self._error(f"Expected a value after '=' for variable '{name}'")

        value = self._parse_expression()

        if not self._match(TokenType.SEMICOLON):
            self._error(f"Expected ';' after declaration of '{name}'")

        return AssignmentNode(name, value)

    def _parse_assignment(self):
        name = self._advance().lexeme

        if not self._match(TokenType.ASSIGN):
            self._error(f"Expected '=' after variable name '{name}'")

        if self._check(TokenType.SEMICOLON):
            self._error(f"Expected a value after '=' for variable '{name}'")

        value = self._parse_expression()

        if not self._match(TokenType.SEMICOLON):
            self._error(f"Expected ';' after assignment to '{name}'")

        return AssignmentNode(name, value)

    def _parse_print(self):
        if self._check(TokenType.SEMICOLON):
            self._error("Expected a value after 'print'")

        expression = self._parse_expression()

        if not self._match(TokenType.SEMICOLON):
            self._error("Expected ';' after print statement")

        return PrintNode(expression)

    def _parse_expression(self):
        return self._parse_addition()

    def _parse_addition(self):
        left = self._parse_multiplication()

        while self._match(TokenType.PLUS, TokenType.MINUS):
            operator = self._previous().lexeme
            right = self._parse_multiplication()
            left = BinaryOpNode(operator, left, right)

        return left

    def _parse_multiplication(self):
        left = self._parse_factor()

        while self._match(TokenType.MULTIPLY, TokenType.DIVIDE):
            operator = self._previous().lexeme
            right = self._parse_factor()
            left = BinaryOpNode(operator, left, right)

        return left

    def _parse_factor(self):
        if self._match(TokenType.NUMBER):
            token = self._previous()
            value = float(token.lexeme) if "." in token.lexeme else int(token.lexeme)
            return NumberNode(value)

        if self._match(TokenType.IDENTIFIER):
            return VariableNode(self._previous().lexeme)

        if self._match(TokenType.LEFT_PAREN):
            expression = self._parse_expression()

            if not self._match(TokenType.RIGHT_PAREN):
                self._error("Expected ')' after expression")

            return expression

        token = self._current()
        raise ParserError(
            f"Expected an expression, but found '{token.lexeme}' "
            f"at line {token.line}, column {token.column}"
        )

    def _match(self, *token_types):
        for token_type in token_types:
            if self._check(token_type):
                self._advance()
                return True

        return False

    def _check(self, token_type):
        if self._at_end():
            return token_type == TokenType.EOF

        return self._current().token_type == token_type

    def _advance(self):
        if not self._at_end():
            self.position += 1

        return self._previous()

    def _current(self):
        if self.position >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[self.position]

    def _previous(self):
        return self.tokens[self.position - 1]

    def _at_end(self):
        if self.position >= len(self.tokens):
            return True

        return self.tokens[self.position].token_type == TokenType.EOF

    def _error(self, message):
        token = self._current()
        raise ParserError(
            f"{message} (line {token.line}, column {token.column})"
        )
