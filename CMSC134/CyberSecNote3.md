---
date_created: 2024-02-20
date_modified: 2024-02-20
type: lecture notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "3"
---

# Introduction to Cryptography
## CS 161
- very tricky to get right
- require great attention to detail and may have hundreds of possible pitfalls
	- private info might leak through side channels
	- primitives might lose all security if used the wrong way

### Brief History
- *cryptography* comes from (Latin) *crypt* (secret) and *graphia* (writing)
	- literally secret messages
- 2000ya Julius Caesar implemented “*Caesar cypher*”, which is a shift crypt
- *”Mechanical era”* arose from German Enigma machine, broken during WWII
	- replica of enigma machine from poland
	- Turing  
- *”Modern cryptography”*
	- Claude Shannon following WWII
	- standardized cryptosystem DES

### Keys
- most basic building block of any cryptographic system
- required by most cryptographic algorithms or functions to lock or unlock secret value
- two main key models in modern cryptography:
	- **symmetric key model**
		- Alice and Bob both know secret key val
		- secure comms using shared key
	- **assymmetric key model**
		- each person has a secret key and corresponding public key

### Definitions
- three main security properties (CIA triad)
- ensure authenticity and integrity via special seal like checksum
- sample scenario:
	- if mallory attempts to alter message in envelope with seal, seal will be broken
	- without the stamp, mallory cannot create her own seal
	- when bob receives message, he can check if the seal is untampered before unsealing the envelope
#### Confidentiality
- prevents adversaries from reading our data
- most crypto algorithms guarantee this with the following:
	- Alice uses a key → encrypt message
	- encrypted message → insecure channel → Bob
	- Bob decrypts message with key
- we call message *plaintext*
- encrypted message as *cyphertext*
- only bob should be able to read plaintext
#### Integrity
- attackers should not be able to change data in message
	- if changed during transmission, this should be detected
#### Authenticity 
- ensure that Alice sent the message
- detect if it was Alice that sent the message, not an attacker via checksum?
#### Deniability
- disallow identifiability of a message’s author, even with checksum present

### Overview of Schemes

|  | Symmetric-key | Asymmetric-key |
| ---- | ---- | ---- |
| Confidentiality | Block ciphers with chaining modes (e.g., AES-CBC) | Public-key encryption(e.g., El Gamal, RSA encryption) |
| Integrity and authentication | MACs (e.g., AES-CBC-MAC) | Digital signatures (e.g., RSA signatures) |

#### Symmetric key
- alice uses `key` → encrypt message → bob uses `key` → decrypt message
- *message authentication codes (MACs)* provide [[CyberSecNote3#Authenticity | Authenticity]] and [[CyberSecNote3#Integrity| Integrity]]
	- shared secret key used to generate MAC on a message
	- receiver uses same secret key to verify MAC
	- [checksum](https://man.archlinux.org/man/sha256sum.1.en)
#### Assymmetric key 
- bob generates pub and private key
- public key shared with alice
- alice use `bob pub key` → encrypt message → bob uses `bob priv key` → decrypt message
- *public key signatures (digital signatures)* for A & I
	- alice also generates pub and priv key
	- alice use `alice priv key` → append to encrypted message → bob use `alice pub key` to verify appended checksum?

### Primitives
- dont guarantee CIA, desirable nevertheless
- *Cryptographic hashes*
	- provide a one way digest
	- irreversible, but verifiable if has hash
- *Pseudo random number generator*
	- many cryptographic systems need a lot of random bits
	- to speed this up, take small amount of true randomness
		- stretch this out into a long sequence indistinguishable from true random data
- *Key exchange schemes*
	- e.g.: [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
	- allow A and B to use insecure comms channel to agree on a shared secret key for symmetric-key encryption

### Kerckhoff’s Principle
- cryptosystems should remain secure even when attacker knows all internal details
- key should be the only thing kept secret
- system must be designed to make it easy to change leaked keys
- assumes that the attacker knows the encryption and decryption algorithms
### Threat models
there are several possibilities about how much access an eavesdropping attacker E has to the insecure channel
- *ciphertext-only attack*
	- E intercepts a single encrypted message and wishes to recover plaintext
- *known plaintext attack*
	- E has intercepted encrypted message and partial information about plaintext
	- we consider E to have full knowledge of plaintext when this happens
- *replay attack*
	- E captures encrypted message from A to B
	- E may not know decrypted message, but E can spam message
- *chosen-plaintext attack*
	- E makes A encrypt arbitrary messages of E’s choice
	- E observes ciphertexts sent by A
	- E can intercept future A comms and 
- *chosen ciphertext attack*
	- E tricks B to decrypt some ciphertexts
	- E can use this to learn about the nature of the cryptographic algorithm
- *chosen-ciphertext / plaintext attack*

## Symmetric-Key Encryption
### IND-CPA Security 
- indistinguishability of ciphertexts under chosen-plaintext attack
- a more formal rigorous definition of confidentiality is:
	- the ciphertext $C$ should give the attacker no additional information about the message $M$
	- attacker should not be able to learn any new info beyond what they already see in $M$
- further formalize this with the experiment:
	- A sends either $M_0$ or $M_1$
	- E tries to guess which by looking at $C$
	- E should be unable to distinguish between $M_0$ or $M_1$

#### Formalized IND-CPA Game
- E must creates two messages, $M_0$ and $M_1$ (plaintexts) and sends both to A
- A at 50% encrypts either $M_0$ or $M_1$ 
	- A chooses a bit $b \in \{0, 1\}$ and encrypts $M_b$
	- sends encrypted message $Enc(K, M_b)$ back to E
- E is now allowed to ask A for encrypted messages of E’s choosing
	- E can send plaintext to A, sending back the ciphertext with secret key
	- E can repeat this as many times as E wants
	- *chosen plaintext attack*
- E must now guess whether ciphertext from step 2 is $M_0$  or $M_1$ in plaintext

- If E can guess which message was sent with > 50% probability, it is not IND-CPA secure.
- $M_0$ and $M_1$ must be of the same length
- ciphertexts are allowed to reveal the length of the plaintext because it is too expensive of a tradeoff to set a constant length for **ALL** ciphertexts

### XOR review
- symmetric key encryption relies on the bitwise XOR $\oplus$ 
#### Def XOR
- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$
Given this definition, we can derive some useful properties

- $x \oplus 0 = x$            0 is the identity
- $x \oplus x = 0$            x is its own inverse
- $x \oplus y = y \oplus x$      commutative property
- $(x \oplus y) \oplus z = x \oplus (y \oplus z)$        associative property
- $x \oplus y \oplus x = y$      x is canceled out

it is also possible to perform algebra with XOR
- $y \oplus 1 = 0$                        goal: solve for y
- $y \oplus 1 \oplus = 0 \oplus 1$               XOR both sides by 1
- $y = 1$                              simplify left-hand side

### One Time Pad (OTP)
- A and B share an $n$-bit secret key $K = k_{1}...k_n$
- bits $k_1,...,k_{n}$ are picked uniformly at random

Suppose Alice wishes to send the n-bit message $M = m_{1}...m_n$
desired properties:
- scramble up message, map to ciphertext $C = c_1...c_n$
- Given knowledge of secret key $K$, easily recover $M$ from $C$
- E who does not know $K$ should get no info from $M$

One time pad is simple: $c_{j}= m_{j} \oplus k_{j}$
decryption algorithm by doing some algebra:
$c_{j}= m_{j}\oplus k_{j}$
$c_{j}\oplus k_{j}=m_{j}\oplus k_{j}\oplus k_{j}$
$c_{j} \oplus k_j= m_{j}$

OTP is done by three procedures
- A and B pick random n bit $K$
- Encryption: $C = M \oplus K$
- Decryption: $M = C \oplus K$

If $K$ is reused, attacker can learn:
- $C \oplus C' = M \oplus M'$
- if attacker learns what M is, they can learn what K is


### Block Ciphers
- A and B share $K$ and repeatedly use this to send $C$
- $n-bit\ C \rightarrow n-bit\ M$
- $2^{k}$ settings for scrambling
- $k-bit$ key to determine scrambling setting
#### Operations
- encryption
	- n-bit input and k-bit key as input
	- n-bit ciphertext as output
- decryption



## CS 134
