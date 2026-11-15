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
