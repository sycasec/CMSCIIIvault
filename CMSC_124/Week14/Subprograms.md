[[CMSC_124]]

# Subprogram
```toc
```

- self contained unit of code that performs a specific task and can be called or executed by another program

## General Subprogram Characteristics
- each program has a single entry point
- only one subprogram is executed at a time 
- control is always returned to the caller when the subprogram execution terminates

### Basic Characteristics
- **Definition** -  describes the interface towards and the actions of the subprogram
- **Call** - request that the subprogram be executed
- **Header** - specifies the kind of subprogram, provides name for sp, provides list of params
- **body** - defines its actions
- **param profile** - contains the number, order, and types of its formal params
- **protocol** - contains the param profile and return type, defines subprogram type

## procedures and functions
### procedures
- subprograms that do not return a value
- change variables accessed without formal params
- change params through args passed by reference
### funcs
- like procedures but functionally modeled to mathematical functions
- call name alongside actual params
- return a value which replaces the call itself

## design issues
- **param passing**
	- multiple ways of doing param passing
	- closely related is whether types of actual params are type checked to formal params of sp
- **are local bars statically or dynamically allocated**
	- ???
- **can sp's be nested, become higher order?**
	- referencing environment becomes an issue
- **restriction of side effects**
	- 