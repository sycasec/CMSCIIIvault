---
date_created: 2024-03-08
date_modified: 2024-03-08
type: lecture notes
course number: CMSC 134
course title: Certificates
entry number: "8"
---

# Certificate
- key distribution is still problematic with previous approaches
## Addressing MITM
- Mallory can intercept Alice and Bob when they are sending public key
## Establishing Key Ownership
### Trusted Directory Service
- an authority sets up a service of giving out public keys
- Alice can query Directory Service **D** for Bob’s public key
- has a number of shortcomings
	- Trust → requires complete trust in D, everyone’s security relies on them
	- Scalability → D becomes a bottleneck
	- Reliability → single point of vulnerability and failure
	- Online → Users will not be able to query D if they are not online
	- Security → needs to be available in real time to answer queries, they need to be carefully secured
- *trust but verify*
	- Alice and Bob should verify the keys they received to check against a rogue keyserver.
### Digital Certificates
- addresses scalability, reliability and online access problems of **TDS**
- a certifying party attests that entity **`E`**’s public key is *`0xdeadbeef`*
	- Signed by certifiying party
	- $\left<M,Sign_{(M,K)}\right>$

**Scenario**:
- David Wagner **D** is an employee of the State of California
- Gov'nuh Jerry Brown **J** signs a “*certificate*” attesting that “David Wagner’s public key is `0xDEADBEEF`”
- Since everyone trusts J, certificate must be legit

- still trust but verify, once signing party's identity is verified, it should be ok
### Public-Key Infrastructure
- Certificate Authority `CA` issues certificates
### Cert Chains and Hierarchical PKI
- Digital Cert but Tree mode
- literally what it says

### Revocation
#### validity periods
- certs can contain an expiration date
#### revocation lists
- CA maintains and publish a list of all revoked certs
- this list is signed and cached locally 


### Web of Trust
- pioneered by PGP for email encryption
- each person certifies public keys of people they trust