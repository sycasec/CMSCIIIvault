# Public Key (Assymetric) Encryption

## Overview
- A and B share secret key K
- requires A and B to coordinate somehow to establish shared secret key
- *Assymetric cryptography* also known as *public-key cryptography* is designed to address this
- B has a public key everyone can access
- A uses B’s public key to encrypt message
- B’s private key will be used to decrypt this message
## Trapdoor$ one-way functions
- difficult to reverse if we do not know $K$
## RSA encryption
- Rivest, Shamir, Adleman
- let $p$ and $q$ be two large primes
- $N = pq$
- let $e$ be any number relatively prime to $(p-1)(q-1)$
- public key is pair: $(N, e)$
- 

Write a program that encrypts and decrypts a message using RSA OAEP
with authenticity

use encrypt-then-MAC scheme for auth encryption

DDL april

must be able to encrypt message using public / priv key
decrypt using private / pub key

establish message authenticity using an integrity key
