import unittest

from src.lexer import Lexer
from src.parser import Parser, ParserError


class TestStatementParser(unittest.TestCase):

    def parse(self, source):
        tokens = Lexer(source).tokenize()

        return Parser(tokens).parse()

    def test_variable_declaration(self):
        program = self.parse("let x = 10;")

        self.assertEqual(
            len(program.statements),
            1
        )

    def test_variable_assignment(self):
        program = self.parse("x = 20;")

        self.assertEqual(
            len(program.statements),
            1
        )

    def test_print_statement(self):
        program = self.parse("print 42;")

        self.assertEqual(
            len(program.statements),
            1
        )

    def test_print_variable(self):
        program = self.parse(
            "let x = 10; print x;"
        )

        self.assertEqual(
            len(program.statements),
            2
        )

    def test_multiple_statements(self):
        source = """
            let x = 10;
            print x;
            x = 20;
            print x;
        """

        program = self.parse(source)

        self.assertEqual(
            len(program.statements),
            4
        )

    def test_expression_in_print(self):
        program = self.parse(
            "print 2 + 3 * 4;"
        )

        self.assertEqual(
            len(program.statements),
            1
        )

    def test_expression_in_assignment(self):
        program = self.parse(
            "let x = 2 + 3;"
        )

        self.assertEqual(
            len(program.statements),
            1
        )

    def test_missing_value_after_equals(self):
        with self.assertRaises(ParserError) as error:
            self.parse("let x = ;")

        self.assertIn(
            "Expected a value after '='",
            str(error.exception)
        )

    def test_missing_variable_name(self):
        with self.assertRaises(ParserError):
            self.parse("let = 10;")

    def test_missing_semicolon(self):
        with self.assertRaises(ParserError):
            self.parse("let x = 10")

    def test_empty_print_statement(self):
        with self.assertRaises(ParserError):
            self.parse("print;")

    def test_missing_closing_parenthesis(self):
        with self.assertRaises(ParserError):
            self.parse("print (2 + 3;")


if __name__ == "__main__":
    unittest.main()
