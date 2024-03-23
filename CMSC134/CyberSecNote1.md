****---
date_created: 2024-02-02
date_modified: 2024-02-14
type: lecture notes
course title: Cyber Security Introduction
course number: CMSC 134
entry number: "1"
---
# CSec Week 2 → 3
```toc
```
## Memory Safety
- most information in a computer has to go through memory
- practical security problems
- memory safety is a concept where attackers cannot read and write to memory 
	- other than those intended by the programmer
	- programs should only be able to access their own respective memory
	- hackers have exploited this before
- when apps are run, the OS doesnt really change that code, just reads and does its job
	- memory unsafe programs can be run
	- REWRITE IN RUST NOW
- a lot of base apps are written in C, which isnt memory safe
## x86 assembly and call stack
- recalling how computers represent values
	- bit (1, 0)
	- nibble - 4 bits \[ (1,0) , (1,0) , (1,0) , (1,0) ]
	- byte - 8 bits, 2 nibbles
	- word - 32 bits / 8 nibs / 4 bytes
- word size depends on CPU architecture
	- in modern times, 64 bit
	- often include defenses against memory vulns
	- focus on 32 bit 
- hex digit used to represent a nibble
- 2 hexes are used to represent a byte
- `0b` before bin digits 
- `0x` before hex digits
- bin 0b1011
- nibble 0xf
- byte 0xe4
### C memory layout
- os reserves address space for the application to store values
- maximum memory is $2^{32}$ bits
	- determined by the size of the register - 32 bits
- memory is represented as top-down grid from 0x00000000 to 0xFFFFFFF
	- top right 0xFFFFFFFF
	- bot left 0x00000000
	- ![[Pasted image 20240202162918.png|360]]
- each row is split into 4 bytes
- int takes one word of memory (specifically `i32`)
	- 4 bytes
	- so if we store it into address 0x00000004
	- it will be stored up until 0x00000007
- in a C program, address space is divided into four sections:
	- **code**
		- contains executable instructions of the program
		- lowest section of reserved memory space
	- **static**
		- constants
		- above the code section
	- **heap**
		- dynamically allocated memory
		- above static section
		- “grows up” to higher addresses
	- **stack**
		- local variables and function calls
		- highest address, “grows down”


#### CPU Registers
- fastest form of memory
	- relatively expensive compared to ram
	- we only have a few of these registers because of cost
- stores one word (4 bytes, 32 bits)
- there are only few, we use names to refer to them instead of addresses
- 3 special registers:
	- **eip**
		- (extended) instruction pointer
		- *stores* address of current instruction in memory
		- when running a program, instructions are loaded into memory at the bottom of memory space
	- **ebp**
		- extended base pointer
		- stores address of the top of the current stack frame
		- stores local variables of the function
		- exists in the stack section of the memory
		- typically higher than the address contained esp
	- **esp**
		- extended stack pointer
		- end of current stack frame
		- typically lower than ebp
	- **General Registers**
	- `eax` and `ebx`
		- temp vars
		- general use
	- stack frame bounded by **esp** and **ebp**
#### Stack
- acts on FILO → literal stack data struct
- in x86, `push` adds a value to the stack
- decrement `esp` to make space
- `pop` takes value off stack
	- read the value at the end of stack
#### Assembly instructions
- mov
- add 
- sub
- push
- pop
### Endian-ness
- little endian
	- 0xd2 → 0x49 
	- least significant to most
- big endian
	- 0x49 → 0xd2


## x86 function calls 
this discusses pointer operations in assembly

- on function call `tl;dr`
	- the stack allocates space to store local variables related to function
	- stack grows down, extra space allocated towards lower addresses in memory
	- upon function end ( `return` ) space on stack is freed
		- the variables are still there though. they will be overwritten eventually.
		- this is the way all memory works (unless format), we can recover deleted files
- FINALLY ON FUNCTION CALL
### Step 1 - Push arguments onto stack
- `eip` currently pointing at instructions of the caller (usually `main()`)
	- this needs to be changed to point to the instruction of the callee (e.g., `foo()` ) 
- `ebp` and `esp` point to the top and bottom of the caller stack frame
- pass arguments of function call into stack
	- right to left, last argument goes in first
- `esp` decremented as we push arguments
### Push the old eip (rip) on the stack 
- this is the address from where we called the function (`foo()`)
- this is also called the `rip`, because we will return to this address after executign `foo()`
- ![[Pasted image 20240213110928.png|525]]

### 3-4 Move `eip`, push old `ebp` (`sfp`) lower
- now we change eip to point towards `foo()` instructions
- we then push the **address** of the old `ebp` below the `rip`
	- also called the `sfp` or *saved frame pointer*
- esp also decremented
	- esp always decremented when we push *any* value onto stack
- ![[Pasted image 20240213111414.png|375]]
### 5-6 Move `ebp` and `esp` down
- now that we have saved the old address for the `ebp`
	- we can safely re-point `ebp` to where `esp` currently is
	- re point ebp to “create” a new “stack-frame” data structure for the function called
	- kind of a “sub-stackframe” inside main
- of course we also re-point `esp`
	- compiler somehow guesses how much to decrement `esp`
	- notes suggest that compiler bases this decision on the amount and type of variables
- ![[Pasted image 20240213114331.png|400]]
### 7 - execute the function
- allocate whatever is in the function
- there will be c code translated to assembly here, execute them all
- ![[Pasted image 20240213114347.png|450]]
### 8 - move esp up
- once the function excecution has ended and has reached a `return`
	- re-point (increment) `esp` to `ebp`
	- anything below esp are considered trash now
- ![[Pasted image 20240213114437.png|375]]
### 9 - restore (pop) old ebp
- we stored the address of the old ebp
	- we just move ebp to that address
	- because it is a pop operation, esp is also incremented
- ![[Pasted image 20240213114452.png|400]]
### 10 restore (pop) old eip
- (re)store old eip address in stack
- now eip points to `main()`
- because it is a pop operation, esp is incremented
- ![[Pasted image 20240213114552.png|400]]
### 11- remove args from stack
- not really remove, more like just ignore them and increment esp
- now esp points to bottom of main stack frame