# SINS Control Structures

## Print Statements

SINS supports print statements, like most coding languages do. To use a print statement, simply type print followed by parentheses and put what you want to print into the parentheses, then add a semicolon to end the line.

Example:

Input-

```sins
let x = 4;

print(x);
```

Output-

```text
4
```

If you want to print words, simply follow the same steps, but put single quotation marks around what you want to print.

Example:

Input-

```sins
print('Hello World');
```

Output-

```text
Hello World
```

## If/Else Statement

SINS supports the If/Else conditional statement. It allows the program to make decisions based on a condition. The If part of the statement checks whether something is true or false. If the if statement is true, it will run the code inside the if statement; if it is false, the code inside the else statement will run instead.

Example:

Input-

```sins
let x = 4;

if (x == 4) {
    print('Hello World');
} else {
    print('Goodbye World');
}
```

Output-

```text
Hello World
```

## While Loops

SINS supports while loops, which allow a section of code to run repeatedly as long as the condition is true. The condition is checked before each iteration of the while loop; if it stops being true, the loop stops immediately.

Example:

Input-

```sins
let x = 5;

while (x <= 10) {
    print(x);
    x = x + 1;
}
```

Output-

```text
5
6
7
8
9
10
```

## Variable Scope

SINS uses something called Variable Scope to figure out where a variable can be used in a SINS program. The variable can be used within the block in which it is created. Say the variable is created inside an if statement; that means the variable can only be used inside that if statement; it doesn't work outside its block.

Example:

Input-

```sins
let x = 500;

if (x == 500) {
    let y = 300;
    print(y);
}

print(x);
```

Output-

```text
300
500
```

So in the created if statement, there is a y. That y can't be used outside of the if statement, if you tried, you would get an error message that the variable doesn't exist. However, since x is just in the program, not a specific block, x can be used after its declaration in the outer program and its nested blocks.

## Additional Feature: A Program End Statement

The additional feature added to SINS will be a statement that ends the program, whether or not it has reached the end. The `end` statement can be used inside other control structures, such as if/else statements or while loops. The `end` statement is a reserved SINS keyword. When a program reaches the `end;` statement, the program immediately stops wherever the statement is located.

Example:

Input-

```sins
let x = 1000;

if (x == 100) {
    print('x is 100');
} else {
    print('x is not equal to 100');
    end;
}

print('This wont print because of the end statement');
```

Output-

```text
x is not equal to 100
```

## Sample Program 2: if/else statement inside while loop

Input-

```sins
let x = 5;

while (x <= 10) {
    if (x == 7) {
        print('this number is seven');
    } else {
        print(x);
    }

    x = x + 1;
}

print('The Program is Finished');
```

Output-

```text
5
6
this number is seven
8
9
10
The Program is Finished
```
