# SINS Final Test Plan

## Complete Feature Programs

| Program | Requirement | Owner | Expected Result | Status |
|---|---|---|---|---|
| `01_arithmetic.sins` | Arithmetic operations | Swopnil | Correct results for `+`, `-`, `*`, and `/` | Pending |
| `02_precedence.sins` | Operator precedence | Swopnil | Multiplication/division before addition/subtraction | Pending |
| `03_variables.sins` | Variables and assignments | Swopnil | Declaration, lookup, and reassignment work | Pending |
| `04_print.sins` | Print statements | Swopnil | Values and expressions print correctly | Pending |
| `05_comparisons.sins` | Comparison operators | Swopnil | Correct Boolean comparison results | Pending |
| `06_if_else.sins` | Conditional statements | Nathaniel | Correct branch executes | Pending |
| `07_while.sins` | While loops | Nathaniel | Loop repeats and terminates correctly | Pending |
| `08_functions.sins` | Functions, parameters and returns | Ian | Function produces the expected return value | Pending |
| `09_scope.sins` | Global and local scope | Ian | Local shadowing does not overwrite the global value | Pending |
| `10_strings.sins` | Strings extension | Ian | Strings, escapes, and concatenation work | Pending |

## Intentional Error Programs

| Program | Error category | Owner | Expected Result | Status |
|---|---|---|---|---|
| `error_invalid_character.sins` | Lexical error | Nathaniel | Clear invalid-character message | Pending |
| `error_invalid_syntax.sins` | Syntax error | Nathaniel | Clear parser error message | Pending |
| `error_undefined_variable.sins` | Runtime error | Ian | Clear undefined-variable message | Pending |
| `error_division_by_zero.sins` | Runtime error | Ian | Clear division-by-zero message | Pending |

## Automated Tests

Run from `part5-functions`:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

All automated tests must report `OK`.

## Complete Program Testing

Run from `part5-functions`:

```bash
find tests -maxdepth 1 -type f -name '[0-9][0-9]_*.sins' -print | sort |
while IFS= read -r file; do
    echo "===== $file ====="
    python3 run_interpreter.py "$file"
done
```

## Error Testing

Run each error program separately:

```bash
python3 run_interpreter.py tests/error_invalid_character.sins
python3 run_interpreter.py tests/error_invalid_syntax.sins
python3 run_interpreter.py tests/error_undefined_variable.sins
python3 run_interpreter.py tests/error_division_by_zero.sins
```

Each command should display a clear error message. An intentional error result is considered successful when the correct error is detected and explained.

## Final Verification

Before creating the submission ZIP:

- Confirm all ten complete programs exist.
- Confirm all four intentional-error programs exist.
- Confirm all automated tests pass.
- Compare every program’s output with its expected result.
- Update each `Pending` status to `Passed`.
- Confirm the README contains reproducible commands.
- Confirm the report accurately states the final test results.
