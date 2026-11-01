# SINS Parser AST Examples

## Example 1: Operator Precedence

### Source

```sins
let x = 2 + 3 * 4;
print x;

```

### AST Output

```text
ProgramNode(statements=[AssignmentNode(name=x, value=BinaryOpNode(operator='+', left=NumberNode(value=2), right=BinaryOpNode(operator='*', left=NumberNode(value=3), right=NumberNode(value=4)))), PrintNode(expression=VariableNode(name=x))])
```

The multiplication operation is nested inside the addition operation, demonstrating that multiplication has higher precedence.

## Example 2: Parenthesized Expression

### Source

```sins
let y = (2 + 3) * 4;
print y;
```

### AST Output

```text
ProgramNode(statements=[AssignmentNode(name=y, value=BinaryOpNode(operator='*', left=BinaryOpNode(operator='+', left=NumberNode(value=2), right=NumberNode(value=3)), right=NumberNode(value=4))), PrintNode(expression=VariableNode(name=y))])
```

The addition operation is evaluated first because it is enclosed in parentheses.

## Example 3: Multiple Operators

### Source

```sins
let total = 20 / 5 - 1;
print total;
```

### AST Output

```text
ProgramNode(statements=[AssignmentNode(name=total, value=BinaryOpNode(operator='-', left=BinaryOpNode(operator='/', left=NumberNode(value=20), right=NumberNode(value=5)), right=NumberNode(value=1))), PrintNode(expression=VariableNode(name=total))])
```

The division operation is nested inside the subtraction operation, demonstrating that division has higher precedence.
