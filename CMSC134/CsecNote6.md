# Pseudorandom Number Generators
## Randomness and Entropy
- in cryptopgraphy when we say “random”, we usually mean “**random and unpredictable**” 
- formalize this by defining *entropy*
	- uniform distribution produces greatest entropy
- this unbiased randomness is computationally expensive
## Pseudorandom Number Generators (pRNGs)
- deterministic
- takes truly random input `seed` → long sequence of pseurdorandom bits
- running the same seed will generate same pseudorandom output
- defined by the following functions:
	- **Seed(entropy)**: take some initial truly random entropy and initialize the pRING’s internal state
	- **Reseed(entropy)**: take in some additional truly random entropy, updating the pRNG’s internal state as needed 
	- **Generate(n)**: generate $n$ pseudorandom bits, updating the internal state as needed
## Rollback Resistance
- even if the attacker knows how function used to generate the pseudorandom output
	- he should not be able to learn anything about the original input
	- one way
# Key Exchange
## Diffie-Hellman Intuition
- A and B share a secret color of paint
	- A selectes amber
	- B selects blue
	- mix when sending to each other
- to hide this, use a publicly known common paint color : green
- mix green with each color
- A receives green + blue 
	- + amber
- B receives green + blue + amber
- E cannot get this because the only thing that was sent over the channel were:
	- green amber 
	- blue green
	- no knowledge of blue (it was already mixed)
	- it would be hard to get the original key of B
## Discrete logarithm problem
- the color analogy relies on the facts that:
	- mixing two colors is easy
	- separating a mixture of two colors to get the original ones is practically impossible
- equivalent of this is one way function
- cannot be solved, NP complete (discrete log)
- $f(x) = g^x(mod\ p)$
	- $p$ is a large prime
	- $g$ is a specially chosen generator
	- it is easy to calculate $f(x)$
		- NP complete to solve for $x$
## Protocol
In high level terms, the Diffie-Hellman key exchange works like this
- A and B first establish the public parameters $p$ and $g$.
- $p$ is a large prime
- $g$ is a generator in the range $1 < g < p - 1$.
- Alice could pick $p$ and $g$ and then announce it publicly Bob
	- Today $g$ and $p$ are often hardcoded or defined in a standard so no need to choose 
	- Does not need to be specific in any way, not secret
- **A** picks a secret value $a \in {0,1,...,p-2}$ 
	- compute $A = g^{a}\ mod\ p$
- **B** picks a secret value $b \in {0,1,...,p-2}$ 
	- compute $B = g^{b}\ mod\ p$
- **A** announces the value $A$ (keeping $a$ secret)
- **B** announces the value $B$ (keeping $b$ secret)
- **A** uses her knowledge of $B$ and $a$ to compute
	- $S = B^{a}=(g^{b})^{a}=g^{ba}$
- symmetrically, **B** uses her knowledge of $A$ and $b$ to compute
	- $S = A^{b}=(g^{a})^{b}=g^{ba}$
- Note that $g^{ba}=g^{ab}\ (mod\ p)$, so A and B end up with the same result, S.
- Finally A and B can use $S$ as a shared key for a symmetric-key cryptosystem

There is no efficient algorithm to deduce $S = g^{ab}\ mod\ p$ from values.
Hardness of this problem is closely related to the discrete log problem discussed.
Fastest known algorithms to solve this problem take $2^{cn^{1/3}(log\ n)^{2/3}}$
## Elliptic 
The commonly used variation of Diffie-Hellman
based on the math of elliptic curves instead of modular arithmetic
More complicated math, but uses smaller keys than modular arithmetic DH
- A and B start with a public known point on the elliptic curve $G$
- A chooses a secret integer $a$
- B chooses a secret integer $b$
- A computes $A = a \cdot G$
	- this is a point on the curve $A$
	- obtained by adding the point $G$ to itself $a$ times
- B does the same thing
- A sends $A$ to B and B sends $B$ to A

- A computes
	- $S = a \cdot B = a \cdot b \cdot G$
- B computes
	- $S = b \cdot A = b \cdot a \cdot G$
