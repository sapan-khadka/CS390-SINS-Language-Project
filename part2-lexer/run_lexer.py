"""Command-line runner for the SINS lexer."""

import sys
from pathlib import Path

from src.lexer import Lexer, LexerError


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 run_lexer.py <source-file.sins>")
        return 1

    source_path = Path(sys.argv[1])

    if not source_path.is_file():
        print(f"Error: File not found: {source_path}")
        return 1

    try:
        source_code = source_path.read_text(encoding="utf-8")
        tokens = Lexer(source_code).tokenize()

        for token in tokens:
            print(token)

        return 0

    except LexerError as error:
        print(f"Lexical error: {error}")
        return 1

    except OSError as error:
        print(f"Error reading file: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
