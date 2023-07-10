[[CMSC_125_Root]]
# Introduction to Operating Systems

```toc
```
## What is an operating system?
- a program that acts as an intermediary between a user of a computer and the computer hardware
- *provides an environment* in which the user can execute programs in a convenient and efficient manner
	- (Silberschatz & Galvin, 1994)
- a *system program* that is implemented in either software (written or Read only memory) or firmware
- set of procedures for driving the resources of the system
	- (Albacea, 2002)

![[Pasted image 20230226233458.png|550]]

- The operating system is an interface between the user and the com

### The OS as a resource allocator
- manager of resources 
	- CPU time
	- memory space
	- file storage space
	- I/O devices
- allocates them to specific programs/users as necessary
- OS should decide which requests are allocated the resources should there be conflicting requests

### Why are OS introduced and developed
- provide a convenient environment for the development and execution of programs
- schedule computational activities to insure good performance of the computing system

### Basic services offered by the OS
- convenient I/O operations
- CPU scheduling 
- memory management
- file systems
- protection and security
- communication and resource sharing
- utilities
- command interpreter

## Evolution of the Operating System
### Early Systems
- Physically large machines run from a console
- programmers were also the operators of the computer system
- instructions were in machine language
- punch cards were fed into the system
- single-user and interactive
- Rise of assemblers, loaders, and linkers to solve the problem of programming in machine language
- libraries for common function
- card readers, line printers, magnetic tapes replacing console
- device drivers for I/O devices
- language translators which brought convenience and complexity

#### Example - run a program in cobol
- load cobol compiler from magnetic tape into computer memory
- initiate execution of cobol compiler
- compiler will then read cobol program 
- compiler will write the assembler equivalent of cobol program into magnetic tape
- load assembler from the magnetic tape into the  computer’s memory and initiate execution
- output binary object of the program from the assembler version
- load binary object of the program and initiate execution
- **significant amount of setup time, CPU idle during set-up time.**

### Simple Batch Systems
- to reduce job set-up time:
	-  hire professional operators
		- problem: operator cannot debug the program being loaded
		- dump of memory and registers are taken and given to the programmer, which allows the operator to continue the next job
		- the programmer is left with a difficult debugging problem.
	-  Batching together similar jobs
		- C, F, C, F, C job order (c cobol, f fortran)
		- batch this together as  C C C F F
		- improved utilization but CPU is still idle during transition from one job to another
	- automatic job sequencing
		- procedure for automatically transferring control from one job to the next
		- ![[Pasted image 20230227014954.png|275]]
		- resident monitor was implemented for this purpose
	- **control cards**
		- contain directives to the resident monitor indicating which program to run
	- control card interpreter
		- reads and carry outs the instructions on the control card durign execution
	- loader
		- loads programs into memory
	- batch operating system
		- jobs are accumulated when a certain number is reached
		- **disadvantage** - lack of interaction between the user and the job while the job is executed.
		- may have very long turnaround time (delay between job submission and job ccompletion)
		- humans are extremely slow (relative to a computer), which led to the creation of automatic job sequencing
		- CPU is still often idle tho
### Off-line processing
- replace slow card readers and line printers (I/O) with magnetic tapes
- rather than let CPU read directly from the cards, data was copied onto magnetic tape
- card readers and line printers were operated offline rather than by the main computer
#### advantage
- main computer no longer constrained by the speed of the card reader & line printer but with the speed of magnetic tapes
- using multiple reader-to-tape and tape-to-reader systems for one CPU
#### disadvantage
- longer delay in getting a job run

### Spooling
- in using tapes, the card reader could not write onto one end of the tape while the CPU read the other end.
- tapes are by nature sequential-access device.
- disk systems are introduced to eliminate this problem, since it is a random-access device.
- Simultaneous Peripheral Operation On Line
- uses a disk as a large buffer, for reading as far ahead as possible on input device and for storing output files until the output devices are able to accept them
- processing data at remote sites
- ![[Pasted image 20230303095319.png|500]]
- overlaps I/O of one job with the computation of other jobs
- computation of one job can overlap with the I/O of other jobs
- can keep both CPU and I/O devices working at a much higher rate
- ****