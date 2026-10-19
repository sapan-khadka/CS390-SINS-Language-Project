"""Command-line runner for the SINS interpreter."""

import sys
from pathlib import Path

from src.lexer import Lexer, LexerError
from src.parser import Parser, ParserError
from src.interpreter import Interpreter
from src.runtime_errors import SINSRuntimeError


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 run_interpreter.py <source-file.sins>")
        return 1

    source_path = Path(sys.argv[1])

    if not source_path.is_file():
        print(f"Error: File not found: {source_path}")
        return 1

    try:
        source = source_path.read_text(encoding="utf-8")
        tokens = Lexer(source).tokenize()
        program = Parser(tokens).parse()
        Interpreter().interpret(program)
        return 0

    except LexerError as error:
        print(f"Lexical error: {error}")
        return 1

    except ParserError as error:
        print(f"Syntax error: {error}")
        return 1

    except SINSRuntimeError as error:
        print(f"Runtime error: {error}")
        return 1

    except OSError as error:
        print(f"File error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
