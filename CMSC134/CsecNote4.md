---
date_created: 2024-02-23
date_modified: 2024-02-23
type: lecture notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "4"
---

# Symmetric-Key Cryptography
## Block Ciphers
- as seen in OTP, regenerating a key for *every* encryption is difficult and expensive.
- instead, A and B share a secret key used to Encrypt and Decrypt messages
- fixed length n-bit plaintext → fixed length n-bit ciphertext
- $2^k$ settings for scrambling
	- k-bit key and n-bit plaintext as input
- each key corresponds to a different scrambling setting
- attacker who doesnt know key wont know the scrambling setting
	- no decryption / encryption
- bijective mapping from p → c
	- one to one, deterministic
	- not one way
### operations
- `enc`: n-bit plaintext + k-bit key → n-bit output
- `dec`: n-bit ciphertext + k-bit key → n-bit plaintext
- today the most commonly used is **Advanced Encryption Standard** (AES)
	- n = 128 bits, k = 128/192/256 bits
	- 1998, Joan Daeman and Vincent Rijmen
	- belgian researchers for a NIST competition
### security
- not IND-CPA secure because deterministic
- behaves like a random permutation on  n-bit strings
### ECB Mode
- electronic code book
- $M$ broken into n-bit blocks
	- each encoded with block cipher
	- whole cipher is just concat of these individual blocks
	- leaks information, because some blocks with the exact same input will have the exact same output
	- hello world hello → sdzkx kzpjxj sdzkx
	- leaks info about plaintext
- ![[Pasted image 20240223130116.png|450]]

### CBC Mode
- cipher block chaining
- popular mode
- for each message pick random n-bit string called `initial vector`
	- $C_{0}= IV$
	- necessary because each successive block factors in the previous block for encryption
- $i^{th}$ ciphertext block is given by $C_{i}=E_{K}(C_{i-1}\oplus M_{i)}$.
- decryption is given by $P_{i}=D_{K}(C_{i})\oplus C_{i-1}$
- ![[Pasted image 20240223131307.png|525]]

### CFB Mode
- Ciphertext Feedback mode
-  $i^{th}$ ciphertext block is given by $C_{i}=E_{K}(C_{i-1})\oplus M_{i}$.
	- current block = encrypt previous block with key then XOR with current block of plaintext
-  decryption is given by $P_{i}=E_{K}(C_{i-1})\oplus C_{i}$
- ![[Pasted image 20240223131628.png|500]] 

### OFB mode
- Output Feedback Mode
- the initial vector IV is repeatedly encrypted to obtain a set of values $Z_i$
- $Z_{0}=IV$
- $Z_{i}=E_K(Z_{i-1})$
- $Z_i$ values used as though they were key for one-time pad
	- $C_i=Z_{i}\oplus M_i$
- so we encrypt all first
- then we XOR each encrypted block with each plaintext block
- concat them all and we have the ciphertext
- $P_i=C_{i}\oplus Z_i$
- ![[Pasted image 20240223132105.png|500]]

### CTR Mode
- counter mode
- counter is initialized to IV and repeatedly incremented and encrypted 
	- obtain a sequence that can now be used as though they were the keys for a one-time pad
- $Z_i=E_{K}(IV+i)$
- $C_i=Z_{i}\oplus M_i$
- decryption 
	- $M_{i}=E_{K}(IV+i)\oplus C_{i}$
- ![[Pasted image 20240223132330.png|575]]

### Parallelization
- CBC mode encryption cannot be parallelized.
- CBC mode decryption can be 
- CTR enc and dec can be 

### Padding 
- In CBC mode, if the plaintext length isn’t a multiple of 128 bits, then the last block of plaintext will be slightly shorter than 128 bits.
- Then the XOR between the 128-bit previous ciphertext and the less-than-128-bit last block of plaintext would be undefined–bitwise 
	- XOR only works if the two inputs being XORed are the same length.
- Suppose the last block of plaintext is only 100 bits.
	- What if we just XOR the first 100 bits of the previous ciphertext
	- the 100 bits of plaintext,
	- Ignore the last 28 bits of the previous ciphertext?
	- Now we have a 100-bit input to the block cipher,
		- only takes 128-bit inputs.
		- input is undefined for the block cipher.
	- solution to this problem is to add padding to the plaintext until it is a multiple of 128 bits.
- padding can add ambiguity because we might be unsure how to depad it later
- One correct padding scheme is PKCS#7 padding
	- **Public Key Cryptography Standards**
	- pad the message by the number of padding bytes used.
	- `0000000010111` → `0000000010111111` padded 3 ones → instead `0000000010111333`
		- 3 bytes of padding were needed
		- obvious to remove
### Reusing Initial Vector is Insecure
- ECB mode is not IND-CPA secure because it is deterministic
- Encrypting the same plaintext twice always results in the same output,
	- info leakage
- All the other modes introduce a random initialization vector (IV)
	- ensure that encrypting the same plaintext twice with the same key results in different output.
- Although proper use of CBC and CTR mode are both IND-CPA, insecure use of either mode (e.g. reusing the IV) breaks IND-CPA security
- In CBC mode, the information leakage is contained
- in CTR mode, the leakage is catastrophic
	- CTR mode can be parallelized, but CBC can not
	- tradeoffs

# Hashes
- used to generate fixed-length “*fingerprint*” of the mesage
- any change to the message will change many of the bits of the hash value
	- should have no detectable patterns as to how the output changes based on specific input changes
- should be deterministic
- $H(M)$ twice will result in the same output
- no secret key
- fixed size
- SHA256 always produces 256 bit value

**Usage**
- suppose A and B have a 1GB document
- comparing the two with hash makes it easier, just compare the hashes
## Properties
### One-way
- infeasible to compute original input using the hash function and ANY output.
- **preimage resistant**
### Second preimage resistant
- infeasible to find another input $x'$ such that:
	- $x' \neq x$ but $H(x) = H(x')$
- it must be infeasible (NOT IMPOSSIBLE) to find another input that results in the same hash output
	- not impossible because we want **determinism** 
### Collision resistant
- reverse of the second one
-  $x' \neq x$ but $H(x) = H(x')$

Can be used to sign software
- suppose devs publish ubuntu and its hash
- you download ubuntu and compute its hash
- you compare it to the hash published by devs
	- if same, valid copy
	- if not, someone tryna hack you

## Hash Algorithms
- MD5 (Message Digest 5) broken years ago
- SHA1 broken in 2017
- two primary families of hash algs secure:
	- SHA2
		- SHA-256, SHA-384, SHA-512
	- SHA3
		- SHA3-256, SHA3-384, SHA3-512
- SHA2 vulnerable to length extension
## Lowest-hash scheme
