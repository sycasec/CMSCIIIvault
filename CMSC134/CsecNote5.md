---
date_created: 2024-02-23
date_modified: 2024-02-23
type: lecture notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "5"
---

# MACs
## Integrity and Authenticity
- MACs are meant to counter tampering and spoofing
- guarantee integrity and authenticity (IA)
- are a asymmetric-key cryptographic primitive
- we assume that A and B share $K$ unknown to anyone else
## Def
- keyed checksum of a message, much like a tag
- fixed length (always the same length, no matter message length)
- typically use 128-bit key $K$ and 128-bit tags
- meant to be used to validate messages
	- A sends $\left<M,T\right>$ to B
	- B recomputes $T$ with $K$ and $M$
- formal def
	- $F: \{0,1\}^{k}\times \{0,1\}^* \rightarrow \{0,1\}^n$
## Security properties
- because deterministic, if $M$ is replaced → $T$ will be different
- designed to be secure against known-plaintext attacks
- E cant feasibly reproduce $T$ for unknown message $M$.

## Secure MAC experiment
- M query A for any message → message + tag is sent
- M wins if M creates a valid message + tag that was not sent to A
## AES-EMAC
- AES-CMAC standardized by NIST
- to understand CMAC, first look at EMAC
- $K$ has 256 bits
	- pair of 128-bit AES keys
	- $K = \left<K_1,K_2\right>$
- $M$ decomposed into sequence of 128-bit blocks:
	- $P_1||...||P_n$
- $S_0=0$
	- $S_{i}=AES_{K_{1}}(S_{i-1} \oplus P_{i)}\ \ \ for\ i = 1,2,...,n.$
- provably secure
	- cannot forge valid AES-EMAC for an unseen $M$
## HMAC
- one of the best MAC constructions
- combines MAC and hash
- even with the key, the result is one way
	- cannot reconstruct message from output
- uses several different hashes (SHA256, 384, etc.)
- choice depends on situation
	- HMAC with block cipher
	- we need twice the length of keys used for block cipher
	- Enc with AES_192, use HMAC_SHA_384
- to understand HMAC, lets look at NMAC
	- $NMAC(K_1,K_2,M)=H(K_1||H(K_2||M))$
	- concat $K_2$ and $M$, hash result
	- concat result with $K_1$, hash concat
	- if H is cryptographic and both Ks are unrelated, NMAC is provably secure
- HMAC is a specific version of nmac that only reqs one $K$
	- $HMAC(M,K) = H((K' \oplus opad) || H((K'\oplus ipad)||M)))$
	- supports variable-length key $K$
	- we first transform $K$ to be length n, pad if shorter, hash to make into n
	- two hardcoded pads, inner and outer
	- generates two underlated keys from the single key
		- ensures two keys are unrelated.
	- opad = `0x5c`
	- ipad = `0x36`
## MACs are not confidential
- do not hide $M$
- A and B exchanging non-encypted plaintext $M$ with MAC (tags)

## Authenticated Encryption
- simultaenously garantees confidentiality and integrity
- symmetric key encryption
	- combination of **block cipher** and *MAC*
- suppose an **IND-CPA** secure encrpytion scheme **Enc** that guarantees:
	- confidentiality
	- unforgeable MAC scheme *Mac*
- two approaches
	- **Enc** → *Mac*
		- guarantees *ciphertext integrity*
			- tampering with ciphertext will be detected by MAC
			- original message kept confidential
	- *Mac* → **Enc**
		- does not have *ciphertext integrity*
			- only original message was tagged
			- if message is tampered, detection only after message was decrypted
				- we then verify MAC
- Enc and MAC should use different keys

## AEAD Encryption Modes
- **Authenticated Encryption with Additional Data**
- integrity provided for additional data
	- if there is an additional message “From A to B”
	- 