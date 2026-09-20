"""Tests for the SINS lexical analyzer."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.lexer import Lexer, LexerError


def run_test(name: str, source: str) -> None:
    print(f"\n--- {name} ---")
    print(f"Input: {source}")

    try:
        tokens = Lexer(source).tokenize()

        print("Tokens:")
        for token in tokens:
            print(token)

    except LexerError as error:
        print(f"Lexer Error: {error}")


run_test(
    "Test 1 - Variable Declaration",
    "let x = 10;",
)

run_test(
    "Test 2 - Arithmetic Expression",
    "let result = 10 + 5 * 2;",
)

run_test(
    "Test 3 - Print Statement",
    "print('Hello World!');",
)

run_test(
    "Test 4 - Control Structure",
    "if (x >= 10) { print('Big'); }",
)

run_test(
    "Test 5 - Function",
    "func multiply(a, b) { return a * b; }",
)

run_test(
    "Test 6 - Invalid Input",
    "let x = 10 @ 5;",
)

run_test(
    "Test 7 - End Statement",
    "end;",
)

# Test 8: Decimal number
run_test(
    "Test 8 - Decimal Number",
    "let price = 19.95;",
)
