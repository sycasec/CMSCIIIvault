[[CMSC_125_Root]]

```toc
```
# OS Basic Concepts Third Edition Albacea

## Definition and History

### What is an operating system?
- a first program or *system program* that is implemented in either software or firmware
- an early example like the *Disk Operating System* acts as an interface between the user and the computer hardware.
- Every command issued by the user will be processed and interpreted for execution by the DOS
- metaphorically, the OS can be considered an a household helper that acts as an interface between you and the chores.
- is a set of procedures for driving the resources of the system
- **main objectives explicit**:
	- provide a convenient environment for development and execution of programs
	- schedule computational activities to ensure good performance of the computer system
		- these objectives are not mutually exclusive
		- a compromise is made in the OS to obtain an acceptable level of each objective
- **services provided**
	- Convenient I/O
		- high-level interface called a device driver saves the user from the technical nightmare of trying to understand how I/O devices work
	- CPU scheduling
		- schedules computing time between several processes in execution, makes sure utilization is at maximum
	- Memory management
		- allocates main memory to several processes
	- File systems
		- manages the organization of secondary storage and provides a “file” abstraction
	- Protection and security
		- prevents unauthorized access of applications to user data
	- Communication and resource sharing
		- processes can communicate and cooperate to achieve a task
	- Utilities
		- date and time, accounting utils, programming utils
	- Command interpreter
		- interface between user and computer, high level commands can be issued

#### Summary
- OS is a program implemented in either firmware or software
- acts as an interface between the user and the computer hardware
- provides and executes procedures that improves CPU or resource utilization
- complexity depends on
	- amount of processors, processor speed, RAM speed, etc.
	- provided facilities (interactive use, single use, etc)
	- nature of the applications it supports 
- the first program that gets loaded into memory


###