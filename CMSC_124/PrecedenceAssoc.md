# Precedence Rules and Associativity

```toc
```


## Precedence Rules

The value of an expression depends at least in part of the order of evaluation of the operators in the expression. Rules like PEMDAS, a hierarchy of evaluation priorities for operators is a concept that mathematicians have developed a long time ago. In most programming languages, the same concept is adapted. 
**Operator precedence rules** for expression evaluation partially define the order in which the operators of different precedence levels are evaluated.  The operator precedence rules for expressiona re based on the hierarchy of operator priorities as implemented by the language designer. 

In most languages, operator precedence is based on mathematics (PEMDAS), and also include unary versions of addition and subtraction. Unary addition is called the **identity operator**, because it has no associated oepration and thus has no effect on its operand. Unary subtraction changes a positive operand to negative. In java and C#, unary minus causes an implicit type conversion of `short` and `byte` to `int`.


### Examples
In all common imperative languages, the unary minus operator can appear in an expression either at the beginning or anywhere inside the expression as long as it is parenthesized to prevent it from being next to another operator.

`a + (- b) * c`
is legal

`a + - b * c`
usually is not. In the python scripting language however, this is translated into the first expression presented.

<div style="page-break-after: always; visibilty: hidden">
</div>

Now, consider the following expressions:

`- a / b`
`- a * b`
`- a ** b`

in the first two cases, the relative precedence of the unary minus operator and the binary operator is irrelevant, the order of the evaluation of the two operators has no effect on the value of the expression. In the last case, however, it does matter. In Fortran, Ruby, Visual Basic, Ada, and Python, exponentiation (note that some languages do not support the exponent operator) has higher precedence than unary minus, making it so that:

`- A ** B`   ≡  `- (A ** B)`

### Precedence of arithmetic operators in Ruby and C-based Languages
|         | Ruby         | C -Based                  |
| ------- | ------------ | ------------------------- |
| Highest | **           | postfix ++, --            |
|         | unary +, -   | prefix ++, --, unary +, - |
|         | \* ,  / ,  % | \* ,  / ,  %              |
| Lowest  | binary +, -  | binary +, -               |

The `**` operator is exponentiation, `%` is the modulo operator, `++` and `--` operators are C-based increment and decrement operators.


## Associativity Rules

consider the following expression:

`a - b + c - d`

if the addition and subtraction operators have the same level of precedence, the question of which operator is evaluated first is answered by the **associativity rules** of the language. An operator can have either left or right associativity, meaning that when there are two adjacent operators with the same precedence, the left operator or the right operator is evaluated first. The common rule in most languages is left to right, except that the exponentiation operator sometimes associates right to left.

<div style="page-break-after: always; visibilty: hidden">
</div>

In the Java expression:

`a - b + c`

the left operator `-` is evaluated first.

Exponentiation in Fortran and Ruby is right associative, so in the expression:

`A ** B ** C`

the right operator is evaluated first.

### Associativity rules of common programming languages
| Language          | Associativity Rule                  |
| ----------------- | ----------------------------------- |
| Ruby              | Left: `* , / , + , - ,`             |
|                   | Right: `**`                         |
| C-based languages | Left: `*, /, %, binary +, binary -` |
|                   | Right: `++, --, unary -, unary +`   |

Many compilers for commong languages make use of the fact that some arithmetic operators are mathematically associative. This means that for the compiler, the value of the expression:

`A + B + C`

does not depend on the order of operator evaluation. Most compilers could use this fact and reorder the evaluation of operators, allowing for simple optimizations.  

### Associativity limitations

consider the expression
`A + B + C + D`

where `A` and `C` are very large positive numbers, and  `B` and `D` are negative numbers with very large absolute values. in this situation, `B + A` does not cause an overflow exception, but `A + C` does (memory limit).  Likewise, `B + D` would cause an overflow exception. Because of the limitations of computer arithmetic addition is made to be nonassociative. Therefore, if the compiler reorders these addition operations, it will affect the value of the expression.