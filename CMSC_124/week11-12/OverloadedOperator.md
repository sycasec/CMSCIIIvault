```toc
```
## Operators
- multiplication, div, add, sub
	- +
		- integer
		- floating point
		- string concat
	- this is overloading

its danger to readability is always present!

as a binary operator
a && b

as a unary operator
a = &b

- using the same symbol for two completely unrelated operations is detrimental to readability
- simple keying error of leaving out the first operand for a bitwise AND operation can go undetected by the compiler.

virtually all languages have a similar problem with the overloadd minus operator
it is used as subtraction and unary operator  

## Dangers of user-defined overloading
- becuase of how versatile overloading can be, lack of documentation will make readability suffer

##