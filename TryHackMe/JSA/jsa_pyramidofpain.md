# Pyramid of Pain
[[jsa_root]]
```toc
```

## Hash Values (Trivial)
- is a numeric value of fixed length that uniquely identifies data.
- result of a hashing algorithm
- not considered cryptographically secure if 2 files have the same hash value or digest
- Sec pros usually use hash values to gain insight into a malware sample - maybe the samples have a specific hash attached to it
- 

### MD5 (Message Digest 5?) - defined by RFC 1321
- designed by Ron Rivest in 1992
- widely used with a 128-bit hash value
- **NOT cryptographically secure**
- in 2011, the IETF published RFC 6151 mentioning a number of attacks against MD5 hashes
	- hash collision
### SHA-1 (Secure Hash Algorithm 1) - RFC 3174
- invented by US NSA uin1995
- produces 160-bit hash value string as a 40 digit hexadecimal number
- NIST deprecated the use of SHA-1 in 2011
	- susceptible to brute-force attacks
	- recommended to migrate to SHA-2 and SHA-3
### SHA-2 (Secure Hash Algorithm 2) 
- designed by NIST ( *National Institute of Standards and Technology* ) and NSA in 2001 as successor of SHA-1
- has many variants, the most common being SHA-256
	- returns a hash value of 256-bits as a 64 digit hex number

## IP Address (Easy)
- used to identify any device in a network
- in the PoP ( *pyramid of pain* ) IP addresses are indicated with the color green
- knowledge of an adversary IP can be useful
	- block, drop, or deny inbound requests from IP addresses via firewall
	- **Fast Flux** can be used to hide botnets behind compromised hosts as proxies
		- maybe a C&C server communicates with proxy then send to target 
		- primary concept is have multiple IP addresses associated with a domain name which is constantly changing

## Domain Names (Simple)
- teal colored
- simply maps an IP address to a string
- puny code can be used to use non ASCII characters into the domain name, making it more confusing
- to detect malicious domains, proxy logs or webserver logs can be used
- attackers hide domains under URL shorteners
	- bit.ly
	- goo.gl
	- ow.ly
	- s.id
	- smarturl.it
	- tiny.pl
	- tinyurl.com
	- x.co
- https://www.expandurl.net/ - works for now
## Host Artifacts (Annoying)
- time-consuming for the attacker
- traces or observables that attackers leave on the system
	- registry values
	- suspicious process execution
	- attack patterns or IOCs
	- files dropped by malicious applications
## Network Artifacts (Annoying)
- if you can detect and respond to this threat, attacker must go back and change tactics
- can be any of the ff:
	- user-agent string
	- C2 info
	- URI patterns followed by HTTP POST requests
## Tools (Challenging)
- attacker would most likely give up trying to break into your network
	- or go back and create a new tool that does the same thing
- antivirus sigs (hash), detection rules, and YARA rules can be great for this
- MalwareBazaar and Malshare provides malware samples, feeds, and YARA results
- for detection rules, SOC Prime Threat Detection Marketplace
### Fuzzy Hashing
- perform similarity analysis
- match two files with minor differences based on fuzzy hash values
- SSDeep
- also called *context triggered piecewise hashes*
## TTPs (Tough)
- tactics, techniques & procedures
- the whole MITR ATT&CK Matrix

