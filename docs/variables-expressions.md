# Variables, Assignments, and Expressions

## Variable Declarations

Variables in SINS are declared using the `let` keyword. A variable name must begin with a letter and may contain letters, numbers, and underscores. The declaration ends with a semicolon.

```sins
let x = 10;
let total = 25;
```

## Assignment

The assignment operator `=` changes the value of a variable that has already been declared. The variable name appears on the left side, and its new value or expression appears on the right side. An assignment ends with a semicolon.

```sins
x = 20;
total = x + 5;
```

## Arithmetic Expressions and Precedence

SINS supports addition, subtraction, multiplication, and division using the operators `+`, `-`, `*`, and `/`. Multiplication and division are evaluated before addition and subtraction. Operators with the same precedence are evaluated from left to right. Parentheses may be used to change the evaluation order.

```sins
let result = 2 + 3 * 4;
let grouped = (2 + 3) * 4;
```

In the first expression, multiplication occurs first, producing `14`. In the second expression, the parentheses are evaluated first, producing `20`.

## Comparison Expressions

SINS uses comparison operators to compare two values. A comparison evaluates to either `true` or `false` and may be used as the condition of an `if` statement or `while` loop.

* `==` — equal to
* `!=` — not equal to
* `<` — less than
* `<=` — less than or equal to
* `>` — greater than
* `>=` — greater than or equal to

```sins
x < 20
total == 25
x != total
```

## Sample Program 1: Calculate a Total

This program declares two numeric variables, calculates a total using arithmetic precedence, compares the result with a limit, and prints a value based on the comparison.

```sins
let price = 10;
let quantity = 3;
let total = price * quantity + 5;

print(total);

if (total >= 30) {
    print(1);
} else {
    print(0);
}
```

The program calculates `10 * 3 + 5`, so `total` becomes `35`. It prints `35`, followed by `1` because the comparison `total >= 30` is true.



