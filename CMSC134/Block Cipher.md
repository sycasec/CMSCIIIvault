# Block Ciphers
Generating new keys for each encryption is difficult and expensive. 
Alice and Bob instead share a single secret key to repeatedly encrypt and decrypt messages.
Block cipher is fundamental in implementing a symmetric encryption scheme.

- Transform:  a fixed-length, $n$-bit input →  fixed-length, $n$-bit output
- $2^k$ scrambling settings
- $k$-bit key to determine the scrambling setting

→ Attacker that doesnt know key $K$ cant just guess scrambling mode
→ no decryption

- **`Encrypt()`** : $(n-bit\ plaintext$, $k-bit\ key)$ → 