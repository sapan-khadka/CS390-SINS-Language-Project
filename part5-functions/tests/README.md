# Part 5 Test Programs

Run these commands from the `part5-functions` directory.

## Automated Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Expected result: all 32 tests pass.

## Required Part 5 Programs

### 1. Functions, parameters, and returns

```bash
python3 run_interpreter.py tests/function_test.sins
```

Expected output:

```text
8
```

### 2. Global and local scope

```bash
python3 run_interpreter.py tests/scope_shadowing.sins
```

Expected output:

```text
20
10
```

### 3. Function-local variables

```bash
python3 run_interpreter.py tests/local_variables.sins
```

Expected output:

```text
24
```

### 4. Function without parameters

```bash
python3 run_interpreter.py tests/function_no_parameters.sins
```

Expected output:

```text
Hello from SINS
```

### 5. String extension

```bash
python3 run_interpreter.py tests/strings.sins
```

This program demonstrates string literals, escaped apostrophes, backslashes, newlines, tabs, string concatenation, and mixed string-number concatenation.

## Legacy Regression Programs

The existing arithmetic, variable, comparison, `if/else`, and `while` programs remain in this directory to verify that Part 5 did not break earlier features.
