"""Tests for global and local variable scope."""

import unittest

from src.environment import Environment
from src.runtime_errors import UndefinedVariableError


class TestScope(unittest.TestCase):

    def setUp(self):
        self.global_scope = Environment()
        self.global_scope.define("x", 10)
        self.local_scope = self.global_scope.create_child()

    def test_local_scope_reads_global_variable(self):
        self.assertEqual(self.local_scope.get("x"), 10)

    def test_local_variable_shadows_global_variable(self):
        self.local_scope.define("x", 20)

        self.assertEqual(self.local_scope.get("x"), 20)
        self.assertEqual(self.global_scope.get("x"), 10)

    def test_local_variable_does_not_leak_to_global_scope(self):
        self.local_scope.define("message", "local")

        self.assertEqual(self.local_scope.get("message"), "local")
        self.assertFalse(self.global_scope.contains("message"))

    def test_assignment_updates_nearest_existing_scope(self):
        self.local_scope.assign("x", 30)

        self.assertEqual(self.local_scope.get("x"), 30)
        self.assertEqual(self.global_scope.get("x"), 30)

    def test_assignment_updates_shadowing_local_variable(self):
        self.local_scope.define("x", 20)
        self.local_scope.assign("x", 25)

        self.assertEqual(self.local_scope.get("x"), 25)
        self.assertEqual(self.global_scope.get("x"), 10)

    def test_contains_local_checks_only_current_scope(self):
        self.assertTrue(self.local_scope.contains("x"))
        self.assertFalse(self.local_scope.contains_local("x"))

        self.local_scope.define("x", 20)
        self.assertTrue(self.local_scope.contains_local("x"))

    def test_undefined_variable_raises_error(self):
        with self.assertRaisesRegex(
            UndefinedVariableError,
            "Undefined variable 'missing'",
        ):
            self.local_scope.get("missing")


if __name__ == "__main__":
    unittest.main()

