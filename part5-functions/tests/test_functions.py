import unittest

from src.ast_nodes import (
    AssignmentNode,
    FunctionCallNode,
    FunctionDefinitionNode,
    ReturnNode,
)
from src.lexer import Lexer
from src.parser import Parser, ParserError


class TestFunctionParser(unittest.TestCase):
    def parse(self, source):
        tokens = Lexer(source).tokenize()
        return Parser(tokens).parse()

    def test_function_definition_with_parameters(self):
        program = self.parse(
            "func add(a, b) { return a + b; }"
        )
        function = program.statements[0]

        self.assertIsInstance(function, FunctionDefinitionNode)
        self.assertEqual(function.name, "add")
        self.assertEqual(function.parameters, ["a", "b"])

    def test_function_definition_without_parameters(self):
        program = self.parse(
            "func answer() { return 42; }"
        )
        function = program.statements[0]

        self.assertIsInstance(function, FunctionDefinitionNode)
        self.assertEqual(function.parameters, [])

    def test_return_statement(self):
        program = self.parse(
            "func identity(value) { return value; }"
        )
        return_statement = program.statements[0].body.statements[0]

        self.assertIsInstance(return_statement, ReturnNode)

    def test_function_call_in_declaration(self):
        program = self.parse(
            "let result = add(10, 20);"
        )
        declaration = program.statements[0]

        self.assertIsInstance(declaration, AssignmentNode)
        self.assertIsInstance(declaration.value, FunctionCallNode)
        self.assertEqual(declaration.value.name, "add")
        self.assertEqual(len(declaration.value.arguments), 2)

    def test_standalone_function_call(self):
        program = self.parse("show(5);")
        call = program.statements[0]

        self.assertIsInstance(call, FunctionCallNode)
        self.assertEqual(call.name, "show")

    def test_missing_closing_parenthesis(self):
        with self.assertRaises(ParserError):
            self.parse("let result = add(10, 20;")


if __name__ == "__main__":
    unittest.main()
