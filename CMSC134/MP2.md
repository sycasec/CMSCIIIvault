# Machine Problem 2
Write program that encrypts and decrypts:
- RSA-OAEP
- with authenticity
- encrypt then sign
- diff key for encryption and signing
- separately generate new key-pairs for encryption and signing
- encrypt then sign/verify then decrypt

## What is RSA?
Stands for Rivest-Shamir-Adleman, publicly describing the RSA algorithm in 1977 which was developed secretly in 1973 by Clifford Cocks at British Government Communications Headquarters (*GCHQ*), declassified in 1997. 

The basic principle behind it is that: 
- it is practical to find three very large positive integers $e, d,$ and $n$ such that:
	- with modular exponentiation for all integers $m\ |\ 0 \leq m < n:$  $(m^e)^d \equiv m\ (mod\ n)$. 
- Knowing $e$ and $n$, it can be extremely difficult to find $d$. 
- The symbol $\equiv$ denotes *modular congruence*, meaning $(m^e)^d$ and $m$ have the same remainder when divided by $n$

RSA involves four steps: 
- key generation
- key distribution
- encryption
- decryption

### Key Generation
1. Choose two large prime numbers $p$ and $q$
	- to make factoring harder, $p$ and $q$ should be chosen at random.
	- be both large and have a large difference