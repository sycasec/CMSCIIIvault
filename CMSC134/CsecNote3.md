# Memory Vuln Mitigation
- C and friends are unsafe
- language choice can have compile and runtime checks
- memory safe languages can prevent 100% of memory safety vulns

## Write memory safe code
- do all the checking for the memory accesses yourself

## Exploit Mitigations
### Non executable pages
- ram is stored in pages
- can be marked writable or executable but not both
- prevents executing arbitrary instructions
#### Subverted via:
- overwriting rip with `execv` (syscall)
- overwrite rip with a chain of ROP gadget addresses
	- ROP compilers used to translate code to address jumps in assembly
### Stack Canaries
- detects tampering of `sfp` and `rip`
- inspired by mine canaries
	- miners bring canaries, if toxic gas is in the mine the canary dies first
- typically one word long (32 bit?)
- typically contains null byte to prevent other exploits
- stays the same in a single run
#### Subversion
- attacks outside stack cant be defended
- overwriting local variables 
- targeted writes
	- if we know that we are writing to the `rip`, stack canary does not detect
- canaries can be leaked by printing strings `printf("%s")`
### Pointer Authentication
- in 64-bit architecture
- canary for pointers
- detect for pointer modification
#### why 64?
- we can address 18 exabytes of memory
- in 32 bit, 4 tb memory is addressable
- 42 to bits to address 4 terabytes, 22 is unused

- the 22 bits is replaced with a secret pointer authentication code by the CPU
- before a `push` CPU replaces unused bits with PAC
- on `pop`, cpu confirms PAC is unchanged
#### example
- rip points to 
- `0x00 00 00 12 34 56 78 9A`
- CPU replaced 0 bits with PAC on `push`
- checks for PAC mismatch on `pop`
- on mismatch, crash

#### Robust PAC
- attacker reuses PAC
- have CPU calculate unique PAC for each address
	- have a key and address to generate PAC
	- attacker wont know key so he cant regenerate PAC
#### Subversion
- guess PAC
- find another vulnerability to create a valid pointer
- discover key (0 day?)
- subvert robust pac function

### Address space layout randomization
- randomizes layout of memory every run
- attacker can no longer reliably predict which memory address to overwrite `rip`
- changes in every run, so its very hard to do
#### subversion
- guess lmao
- leak addresses of sections while attacking and use this to target address jumps

## assignment
- read “Smashing the Stack for Fun and Profit”
