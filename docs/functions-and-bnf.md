# Functions & Grammar

## Functions

SINS supports functions via the ```func``` keyword. To create functions, type this keyword, then the name you wish to call the function, and then a set of parenthesis, which may or may not contain some parameters. A set of brackets are used to contain the code inside. ```return``` must be used at the end of every function.

A function can have one or more parameters.
Example:

Input
```sins
let a = 2;
let b = 5;
func multiply(a, b) {
	let x = a;
	let y = b;
	let output = x * y;
	return output;
}

multiply(a, b)
```

Output
```text
10
```

A function can also have no parameters.
Example:

Input
```sins
func noParameters() {
	print('This function has no parameters.');
	return;
}

noParameters();
```

Output
```text
This function has no parameters.
```

As you may have seen already, the ```return``` keyword does not necessarily have to have any parameters specified after it. This can be for when you do not want a function returning any kind of data. (In other words, a function that simply sets some external variables, or maybe a program that only prints something to the console.)

Example:

Input
```sins
func printNumbersRangedInclusive(min, max) {
	let counter = min;
	while (counter <= max) {
		print(counter)
		counter = counter + 1;
	}
	return;
}
let x = 0;
let y = 10;
printNumbersRangedInclusive(x, y);
```

Output
```text
0
1
2
3
4
5
6
7
8
9
10
```

Note: The function does not necessarily need to have input parameters to have a parameter for return.


# BNF

This is the BNF of SINS, which defines how the syntax works.

```bnf
<program> ::= <statement-list>
<statement-list> ::= <statement>
		| <statement> <statement-list>
<statement> ::= <assignment>
		| <reassignment>
		| <print-statement>
		| <if-statement>
		| <while-statement>
		| <function-definition>
		| <function>
		| <end-statement>
<assignment> ::= "let" <identifier> "=" <expression> ";"
		| "let" <identifier> "=" <string> ";"
		| "let" <identifier> ";"
<reassignment> ::= <identifier> "=" <expression> ";"
		| "let" <identifier> "=" <string> ";"
<string> ::= "'" <characters> "'"
<characters> ::= <char> <characters> 
		| ""
<char> ::= <lowercase> 
		| <uppercase> 
		| <digit>
<lowercase> ::= "a" 
		| "b" 
		| "c" 
		| "d" 
		| "e" 
		| "f" 
		| "g" 
		| "h" 
		| "i" 
		| "j"
              	| "k" 
		| "l" 
		| "m" 
		| "n" 
		| "o" 
		| "p" 
		| "q" 
		| "r" 
		| "s" 
		| "t"
              	| "u" 
		| "v" 
		| "w" 
		| "x" 
		| "y" 
		| "z"
<uppercase> ::= "A" 
		| "B" 
		| "C" 
		| "D" 
		| "E" 
		| "F" 
		| "G" 
		| "H" 
		| "I" 
		| "J"
              	| "K" 
		| "L" 
		| "M" 
		| "N" 
		| "O" 
		| "P" 
		| "Q" 
		| "R" 
		| "S" 
		| "T"
              	| "U" 
		| "V" 
		| "W" 
		| "X" 
		| "Y" 
		| "Z"
<digit> ::= "0" 
		| "1" 
		| "2" 
		| "3" 
		| "4" 
		| "5" 
		| "6" 
		| "7" 
		| "8" 
		| "9"
<expression> ::= <term> "+" <expression> 
		| <term> "-" <expression>
		| <term>
<term> ::= <factor> "*" <term>
		| <factor> "/" <term>
		| <factor>
<factor> ::= "(" <expression> ")" 
		| <constant>
<constant> ::= number
<print-statement> ::= "print" "(" [<expression>] ")" ";"
		| "print" "(" [<string>] ")" ";"
<body-block> ::= "{" <statement-list> "}"
<comparison> ::= <expression> <comparison-symbol> <expression>
<comparison-symbol> ::= "<" 
		| ">" 
		| "==" 
		| "<=" 
		| ">=" 
		| "!="
<if-statement> ::= "if" "(" <comparison> ")" <body-block>
		| "if" "(" <comparison> ")" <body-block> "else" <body-block>
		| "if" "(" <comparison> ")" <body-block> "else if" "(" <comparison> ")" <body-block> "else" <body-block>
<while-statement> ::= "while" "(" <expression> ")" <body-block>
<function-body> ::= "{" <statement-list> <return> "}"
<return> ::= "return" [ <expression> ] ";"
<parameter-list> ::= <identifier> "," <parameter-list>
		| <identifier>
<function-definition> ::= <function-definition> ::= "func" <identifier> "(" [<parameter-list>] ")" <function-body>
<function> ::= <identifier> "(" [expression] ")" ";"
<end-statement> ::= "end" ";"
		| "end" "(" <expression> ")" ";"
```
