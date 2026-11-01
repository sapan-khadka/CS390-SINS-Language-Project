"""Tests for the SINS interpreter environment."""

import unittest

from src.environment import Environment
from src.runtime_errors import UndefinedVariableError


class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.environment = Environment()

    def test_define_and_get_variable(self):
        self.environment.define("x", 10)
        self.assertEqual(self.environment.get("x"), 10)

    def test_assign_existing_variable(self):
        self.environment.define("x", 10)
        self.environment.assign("x", 15)
        self.assertEqual(self.environment.get("x"), 15)

    def test_define_replaces_existing_declaration(self):
        self.environment.define("x", 10)
        self.environment.define("x", 20)
        self.assertEqual(self.environment.get("x"), 20)

    def test_contains_variable(self):
        self.environment.define("message", "hello")
        self.assertTrue(self.environment.contains("message"))
        self.assertFalse(self.environment.contains("missing"))

    def test_snapshot_returns_copy(self):
        self.environment.define("x", 10)
        snapshot = self.environment.snapshot()
        snapshot["x"] = 99
        self.assertEqual(self.environment.get("x"), 10)

    def test_get_undefined_variable_raises_error(self):
        with self.assertRaisesRegex(
            UndefinedVariableError,
            "Undefined variable 'missing'",
        ):
            self.environment.get("missing")

    def test_assign_undefined_variable_raises_error(self):
        with self.assertRaisesRegex(
            UndefinedVariableError,
            "Undefined variable 'missing'",
        ):
            self.environment.assign("missing", 10)


if __name__ == "__main__":
    unittest.main()
