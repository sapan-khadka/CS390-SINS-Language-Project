
from .token_types import TokenType
from .ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    AssignmentNode,
    PrintNode,
    BlockNode,
    IfNode,
    WhileNode,
)


class ParserError(Exception):
    """Raised when the parser encounters invalid syntax."""


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

        if self._match(TokenType.IF):
            return self._parse_if()

        if self._match(TokenType.WHILE):
            return self._parse_while()

        if self._match(TokenType.LEFT_BRACE):
            return self._parse_block()

        if self._check(TokenType.IDENTIFIER):
            return self._parse_assignment()

        self._error("Expected a statement")

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

        return AssignmentNode(name, value, is_declaration=True)
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

        # Support both print(expression); and the older print expression;
        parenthesized = self._match(TokenType.LEFT_PAREN)

        expression = self._parse_expression()

        if parenthesized and not self._match(TokenType.RIGHT_PAREN):
            self._error("Expected ')' after print expression")

        if not self._match(TokenType.SEMICOLON):
            self._error("Expected ';' after print statement")

        return PrintNode(expression)

    def _parse_if(self):
        if not self._match(TokenType.LEFT_PAREN):
            self._error("Expected '(' after 'if'")

        condition = self._parse_expression()

        if not self._match(TokenType.RIGHT_PAREN):
            self._error("Expected ')' after if condition")

        then_branch = self._parse_statement()
        else_branch = None

        if self._match(TokenType.ELSE):
            else_branch = self._parse_statement()

        return IfNode(condition, then_branch, else_branch)

    def _parse_while(self):
        if not self._match(TokenType.LEFT_PAREN):
            self._error("Expected '(' after 'while'")

        condition = self._parse_expression()

        if not self._match(TokenType.RIGHT_PAREN):
            self._error("Expected ')' after while condition")

        body = self._parse_statement()
        return WhileNode(condition, body)

    def _parse_block(self):
        statements = []

        while (
            not self._check(TokenType.RIGHT_BRACE)
            and not self._at_end()
        ):
            statements.append(self._parse_statement())

        if not self._match(TokenType.RIGHT_BRACE):
            self._error("Expected '}' after block")

        return BlockNode(statements)

    def _parse_expression(self):
        return self._parse_comparison()

    def _parse_comparison(self):
        left = self._parse_addition()

        if self._match(
            TokenType.EQUAL,
            TokenType.NOT_EQUAL,
            TokenType.LESS_THAN,
            TokenType.LESS_EQUAL,
            TokenType.GREATER_THAN,
            TokenType.GREATER_EQUAL,
        ):
            operator = self._previous().lexeme
            right = self._parse_addition()
            return BinaryOpNode(operator, left, right)

        return left

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
            value = (
                float(token.lexeme)
                if "." in token.lexeme
                else int(token.lexeme)
            )
            return NumberNode(value)

        if self._match(TokenType.IDENTIFIER):
            return VariableNode(self._previous().lexeme)

        if self._match(TokenType.LEFT_PAREN):
            expression = self._parse_expression()

            if not self._match(TokenType.RIGHT_PAREN):
                self._error("Expected ')' after expression")

            return expression

        self._error("Expected an expression")

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
        return self.tokens[self.position]

    def _previous(self):
        return self.tokens[self.position - 1]

    def _at_end(self):
        return (
            self.position >= len(self.tokens)
            or self.tokens[self.position].token_type == TokenType.EOF
        )

    def _error(self, message):
        if self._at_end():
            if self.tokens:
                token = self.tokens[-1]
                raise ParserError(
                    f"{message} (after line {token.line}, "
                    f"column {token.column})"
                )

            raise ParserError(message)

        token = self._current()
        raise ParserError(
            f"{message} (line {token.line}, column {token.column})"
        )

