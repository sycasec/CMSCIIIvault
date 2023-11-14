---
type: notes
date_created: 2023-10-23
date_modified: 2023-10-24
---
# The Data Link Layer
```toc
```

## Introduction
- Layer 2 in the [[DCN_Lecture_1#The OSI Model | OSI Model]]
- Transforms the physical layer a raw transmission facility to a link for node2node comms
### Responsibilities
#### FRAMING 
- divides the stream of bits received from the network layer to manageable data units called **frames** 
#### ADDRESSING
- adds **header** to the frame to define the address of the sender and receiver of the frame
#### FLOW CONTROL
- if *data absorb rate* < *data produce rate*, data link imposes flow control to avoid overflow
#### ERROR CONTROL
- adds mechanisms to detect and retransmit damaged, duplicate, or lost frames
#### MEDIA ACCESS CONTROL
- when two or more devices are connected to the same link, data link protocols are used to determine which device has control over the link at any given time
### Types of Errors
#### SINGLE BIT ERROR
- 1 bit of a data unit (byte, character, packet) is changed from 1 to 0 or 0 to 1
#### BURST ERROR
- two or more bits of data have been changed
## Error Correction
### Redundancy 
- Sends extra (redundant) bits with data
- added by sender and removed by receiver allowing receiver to detect and correct corrupted bits
### Detection vs Correction
- #### DETECTION:
	- check if error has occurred
	- count of errors not included
- #### CORRECTION:
	- detect and correct
	- know the location and number of errors, size of data unit
### Error Correction
- #### FORWARD:
	- receiver tries to guess the mesage using redundant bits
	- ideal if n_errors  is small
- #### Retransmission:
	- receiver detects occurence of error 
	- asks sender to resend the message until no more error
## Coding
- sender adds redundant bits through a certain process 
- creates relationship between redundant bits and actual bits
### Block Coding
- divide message into blocks, each of k bits called *datawords*
- add redundant bits to each block to make the length n = k + r
	- r = *codeword*
#### Error Detection
- receiver has or can find a list of valid codewords
- the original codeword has changed to an invalid one
- can only detect single errors
- two or more errors may remain undetected
- ## Popular Techniques for Error Detection
### Simple Parity-Check
- a k-bit dataword is used to generate a n-bit codeword where n = k+1
	- the the k+1 part is usually appended at the tail of the dataword
	- can detect an odd number of errors (?)
	- tries to make the “ones” even
		- 0000 = 00000
		- 0001 = 00011
		- 0011 = 00110
### Two Dimensional Parity Check
- parity check but twod
- four errors cannot be detected

### Checksum
- also known as hash sum
- created by calculating binary values in a packet or other block of data using algorithm - result is stored with the data (like codeword)
- when data is received at the other end, checksum is recalculated
	- in this example, binary addition is used. each $k$ word of an $n$ - length string is added together
		- using 1’s complement addition
		- this means that an extra 1 is carried, and added to to the string again.
		- after calculating the sum, its inverse is the checksum, and added to the $n$ - length string,
		- turning it into $n + k$  length string
	- upon receiving, each $k$ word of the $n + k$ length string is added together
	- it is expected to have a sum of all ones, this means that the data is uncorrupted.
- this can cause errors such as reordering of bytes, or bit swapping in such a particular way that it will be undetected ultimately.
### Cyclic Redundancy Check
- technique based on binary division
	- single binary string $M$
	- key word $k$
	- $\frac{M}{k} = r$
	- this means that if $\frac{M}{r} = k$ ,the transmission is valid
		- assuming the transmitter sends M and r
	- other algorithms divide $M$ and $r$ with $k$ and check if the remainder is 0

## Framing
- process of separating message from one source to a destination
	- attaches to the message the sender address and destination address
	- this allows the message to be distinguishable from other messages.
- goal: determine the start and end of packets, making each frame distinguishable from one another 
- the data link layer frame includes:
	- Data - packet from the network layer
	- Header - contains information such as addressing (source and destination)
	- Trailer - contains information for error detection or redundant bits
- ![[Pasted image 20231027135157.png]]
## Types of Framing
- **Fixed-Size Framing** 
	- size is fixed
	- no frame boundaries
	- length of frame itself acts as delimiter
- **Variable-Size Framing**
	- prevalent in LANS
	- End of frame and beginning of next needs to be defined
	- Two approaches
		- *Character-Oriented*
		- *Bit-Oriented*
### Character-Oriented Variable-Size Framing
- Byte-oriented
- data carried are 8 bit characters from an encoding (ASCII, UTF-8, etc)
- Header and trailer are also multiple of 8 bits
- an 8-bit flag is added at the beginning and end of frame to separate a frame from the next
	- ![[Pasted image 20231027135707.png]]
- started becoming popular when text was exchanged
- flag must be any character not used for text communication
#### Problem
sending other types of information such as graphs, audio, video, images,
	- the pattern used for the flag could be a part of the information in these formats
#### Solution
- byte stuffing or character stuffing
#### Byte Stuffing
- special byte is added to the data section of the frame when there is a character with same pattern as the flag (escape character)
- the extra byte is usually called the escape character with a predefined bit pattern
	- ![[Pasted image 20231027135721.png]]
- when receiver encounters the escape character, it is removed from the data section and treats the byte or character right next to it as data, not delimiting flag.