from lexer import Lexer, LexerError


def run_test(name, source):
    print(f"\n--- {name} ---")
    print(f"Input: {source}")

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        print("Tokens:")
        for token in tokens:
            print(token)

    except LexerError as error:
        print(f"Lexer Error: {error}")


# Test 1: Variable declaration
run_test(
    "Test 1 - Variable Declaration",
    "let x = 10;"
)

# Test 2: Arithmetic expression
run_test(
    "Test 2 - Arithmetic",
    "let result = 10 + 5 * 2;"
)

# Test 3: Print statement
run_test(
    "Test 3 - Print Statement",
    "print('Hello World!');"
)

# Test 4: Control structure
run_test(
    "Test 4 - Control Structure",
    "if (x >= 10) { print('Big'); }"
)

# Test 5: Function
run_test(
    "Test 5 - Function",
    "func multiply(a, b) { return a * b; }"
)

# Test 6: Invalid input
run_test(
    "Test 6 - Invalid Input",
    "let x = 10 @ 5;"
)