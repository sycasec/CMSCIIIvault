---
date_created: 2024-02-01
date_modified: 2024-02-02
type: notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "0"
---

# Cyber Sec Note 1
``` toc
```

## introduction
- expects the students to:
	- describe coverage of security theory and practice
	- employ security policies, models, and mechanisms related to confidentiality, integrity, authentication, identification, and availability issues related to information and info systems
	- recommend practical solutions to many security issues
- topics:
	- security principles
	- memory safety
	- cryptography
	- web
	- networking
- week 1 → 3
	- principles
	- memory safety
	- GDB? idk
- week 4 → 7
	- cryptography
- week 8 → 10
	- web
		- sql injection
		- xss
	- networking
		- protocols
- heavily adapted from cs 161

## Principles
### Threat model
- model of your attacker
- what resources they have
	- layout capabilities and motive of the threat
- we assume that the attacker can:
	- interact with system undetected
	- has general info of our system
	- persistent in attack and can get lucky
	- has resources to launch attack
	- coordinate complex attacks across systems and networks
	- can target every system that has a computer
### Human Factors
- the weakest link is the human
- PEBCAK still exists despite technological advancement
	- problem exists between chair and keyboard
- people make mistakes
- people like convenience
	- people will look for ways to subvert security and have an easier time
	- lengthy password requirements will cause user to get lazy with pw
	- social engineering works all the time
		- mitigation requires immense resources spent in training all employees
### Security is economics
- you only have so much resources and so many security pain points
- businesses want to maximize profit now, worry about sec later
-  we can only make the most cost efficient decisions about sec
	- nothing is 100% secure.
- thieves will take the easiest loot they can (humans want convenience)
	- best to do the bare minimum security
### Detect if you cant prevent
- we need to at the very least detect an attack
	- we assume that we can never 100% prevent
	- knowing the nature of the attack allows appropriate response
### Defense
- use multiple types of defenses layered together
	- law of diminishing returns applies here, so try to make the most efficient defense to cost ratio
### Least Privilege
- provide the minimum set of privileges for all programs
	- a suspicious calculator app can be used to run reverse shells
### Separation of Responsibility
- split privilege into smaller parts
- no one entity has entire power over the system (`sudo`?)
- drastically reduces chance of attacker taking control of entire system
### Ensure complete mediation
- make sure to double check access control policy
### Shannon’s Maxim
- assume that the attacker completely knows every detail of the system they are attacking
- claims that the concept of security through obscurity does not work
- closely related to **Kerchoff’s Principle**
	- cryptographic systems should remain secure even when the attacker knows all the internal details of the system
### Use fail-safe defaults
- closely rleated to separation of responsibility and least privilege
- make sure that if security of the system crashes, the system defaults to secure behavior
	- if a firewall crashes, just shutdown network connections
		- the opposite would be if the firewall crashes, anything gets throuhg
- attacker cant wait for or induce system failure
### Design sec from the start
- retrofitting security is difficult and costly
### Trusted Computing Base (TCB)
- the system must have a portion that we can trust to operate correctly and securely
- should be as small as possible, making it easier to write and audit for errors
- e.g: your phone
	- lock screen should be part of TCB
	- OS should be part of the TCB
	- physical CPU is part of the TCB
	- email app is not in TCB, since function is not related to security
		- also is relatively more complex in relation to others.
