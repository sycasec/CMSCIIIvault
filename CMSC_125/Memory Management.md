[[CMSC_125_Root]]

```toc
```

# Memory Management

## Memory manager
- determines which ready processes should be stored into memory

### Address Binding
- process must be loaded in memory before execution from disk, which is binary code.
- compiler loads and binds instructions and data from binary executable code to memory addresses.
- *Times Of Binding*
	- **Compile Time**
		- code is loaded at a fixed memory address (absolute code)
		- i.e, user processes will be loaded starting at address 0
	- **Load Time**
		- binding at load time, if address changes while compiling, code is re-loaded (?)
		- code is relocatable
	- **Execution Time**
		- required for memory management schemes
		- code can be relocated during execution
- Most modern OS require execution binding to allow for dynamic memory allocation. 
- Memory managers tend to swap code from main memory to secondary memory

### Logical and Physical Address
- compile & load time address binding = logical & physical addresses are the same
- execution time binding = logical and physical addresses differ (calculation by MMU to translate logical to physical address)
- **Memory Management Unit MMU**
	- 

### MM in early systems
- **Single User Systems**
	- one contiguous chunk of memory was allocated to a user process.
		- the single process does not fully occupy the alloted chunk
		- internal fragmentation from unused memory
	 - some user processes accidentally or intentionally modify chunk occupied by Os
	- size of programs limited to storage reserved for the user processes
		- solved with **Overlays**, a program bigger than the storage reserved for the user process is loaded from secondary storage
		-  a section of the program that is no longer needed is discarded, and the MM system continues to load the rest of the program from the secondary storage.
- **Multiprogramming Systems**
	- several processes with memory requirement exceeding that provided by the system is loaded into memory for a limited amount of time
	- new schemes are made to avoid blocking processes with unloaded code
	- **Multiprogramming with Fixed number of Tasks or OS/MFT**
		- a fixed number of jobs are loaded into memory divided into partitions classified as small-size, medium-size, and large-size
	- **Compaction and Relocation**
		- programs within contiguous chunks of memory are relocated to accomodate for more jobs
		- you already know this
		- *expensive overhead* of shifting processes within main memory
			- consumes CPU time
			- stops every process running while it is performed
			- code of user processes are relocated
		- only possible if processes can be relocated
- **Modern OS**
	- non contiguous memory allocation
	- blocks are smaller in sizes, contiguous chunks may be placed anywhere in memory
	- fragmentation is minimized
	- blocks loaded are directly involved in current execution
	- high multiprogramming, difficult to implement

### MM in Time Sharing
- balance running multiple processes with response time

### Swapping
- processes not using CPU are swapped out for higher priority process
	- stored into secondary storage or cache memory
- **Cache Memory**
	- temporary storage for swa