# Primitive Data Types

#### TOC
1. [[Wk_5_PrimitiveDataTypes#Data Objects|Data Objects]]
2. [[Wk_5_PrimitiveDataTypes#Data Values Types|Data Values & Types]]
3. [[Wk_5_PrimitiveDataTypes#Binding|Binding]]
4. [[Wk_5_PrimitiveDataTypes#Declaration|Declaration]]
5. [[Wk_5_PrimitiveDataTypes#Type Checking Equivalence|Type Checking & Equivalence]]
6. [[Wk_5_PrimitiveDataTypes#Type Conversion Coercion|Type Conversion and Coercion]]



## Data Objects
- represent container for data values
- memory spaces where data are stored and retrieved from
- **programmer-defined**
	- explicitly created
	- manip by programmer through declarations / statements
- **system defined**
	- defined by compiler
	- housekeeping during program execution
	- not directly accessible to programmer

- **Attributes**
	- Value type
	- size
- **Lifetime**
	- how long DO exists
	- when it is created / destroyed


## Data Values & Types
- **primitive type**
	- value is atomic and cannot be decomposed
	- pascal examples
		- character
		- integer
		- real
		- boolean
		- enumerand
- **composite type**
	- values are composed or structured from simpler vals
	- examples:
		- tuples
		- records
		- variants
		- unions
		- arrays
		- sets
		- string
		- list
		- tree
		- relation


##### Primitive Data Type
- **Numeric Data Type**
	- most common are integer and real
	- C:
		- type int has an added attribute for the number of bytes
		- unsigned int (positive ints), long (4 bytes), short (2 bytes)
		- characters are one byte ints
	- Java:
		- more than two int types:
			- byte b: 8 bits
			- short s: 16 bits
			- int i: 32 bits
			- long j: 64 bits
	- FORTRAN:
		- real number has precision attribute
			- single (ex: REAL X;)
			- double (ex: DOUBLE PRECISION Y;)
	- java , c : 
		- float single precision
		- double is double precision
- **subrange type**
	- numeric
	- saves on storage by limiting memory allocation
- **enumeration type**
	- list of constants, contain small set of values
- **boolean type**
	- true or false
- **char type**
	- numeric coding, literal character 
	- most popular coding scheme is ASCII
- **string type**
	- natural extension of char
	- *string* of characters
	- linear array of characters
	
## Binding
## Declaration
## Type Checking & Equivalence
## Type Conversion & Coercion
## Initialization