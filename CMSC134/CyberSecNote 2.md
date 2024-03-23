---
date_created: 2024-02-04
date_modified: 2024-02-04
type: lecture notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "2"
---

# Memory Safety Vulns (week 3)
```toc
```

## Buffer Overflow
- particular risk in C  
- one of the most pervasive kind of implementation flaws around
- C++ and Objective-C suffer from the same vulnerability
### absence of automatic bounds-checking for array or pointer accesses
- hypothetical `char buffer[4]`
	- C will not throw an error if programmer tries to access `buffer[5]`
	- buffer overflows take advantage of this vulnerability
- programmer fails to perform adequate bounds check
	- triggers an out-of-bounds memory access that writes (or reads) beyond the bounds of some memory region
	- attackers use this behavior to expose other values stored in stack frame

lets start with a simple example.
```c
char buf[8];
void vulnerable() {
	gets(buf);
}
```
- ![[Pasted image 20240204230049.png|275]]
- in this example, `gets()` reads as many bytes as user supplies and stores those into `buf[]`
	- if input is more than 8 bytes, write past end of allocated `buf[]` memory
	- this is unintended behavior (bug)
- note that `char buf[8]` is located in the static part of memory (since it is defined outside of the function)
- each row of the diagram represents 4 bytes, `char buf[8]` takes 2 rows 
- `gets(buf)` writes user input from lower addresses to higher addresses
	- starting at `buf[0]`
	- attacker can write beyond `buf[8]` since there is no bounds checking

### to illustrate the danger of this bug:
```c
char buf[8];
int auth = 0;
void vulnerable() {
	gets(buf);
}
```
- since `buf` and `auth` are both defined outside of the function, they are both in static
- in C, static is filled in the order that variables are defined
	- static memory grows upward
	- `buf` was defined first
	- `auth` is at higher mem address than `buf`
- if for example, the `auth` variable is used to login:
	- attacker can write 9 bytes to `buf`
	- this sets `auth = 1`
	- attacker is now logged in
### Function example
```c
char buf[8];
int (*fnptr)();
void vulnerable() {
	gets(buf);
}
```
 fnptr is a dereferenced function pointer, storing the mem address of said function
- calling fnptr will execute whatever function is in that address
- fnptr is once again stored in a higher mem address than buf
	- the exact same exploit
- upon writing 8 bytes to `buf`, attacker can overwrite fnptr with any address
	- called *malicious code infection attack*
	- attacker can store malicious code anywhere in memory

## Stack Smashing
- buffer overrun vuln
- variables in stack
- you already know
- exploits x86 function call convention

### sample vuln code
```c
void vuln() { 
	char buf[8];
	gets(buf);
}
```
- when `vuln()` is called, stack frame is pushed onto stack
- stack will look like something like this:
- ![[Pasted image 20240206125539.png]]
- the problem here is that the attacker could write into the `rip` of `vuln()` itself
	- which changes the rip, allowing attacker to execute malicious code

## Off by one
- sfp last byte is overwritten
```c
void vuln(){
	char buf[8];
	size_t length read_int();
	if (length )
}
```

##