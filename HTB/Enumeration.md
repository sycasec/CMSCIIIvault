---
date_created: 2024-03-21
date_modified: 2024-03-21
type: pentester_notes
topic: Enumeration Principles
---
# Enumeration
``` toc
```
## Enumeration Overview
is a widely used term in cybersecurity that usually stands for information gathering using:
- active methods 
	- scans
- passive
	- 3rd party information providers

- **OSINT** is an independent procedure performed separately from enumeration
	- exclusively based on *passive information gathering*. 

Enumeration is an information gathering loop constantly improving upon gathered data, such as:
- domains
- IP addresses
- accessible services
- many other sources

After identifying target infrastructure, examine individual services and protocols.
- the goal of enumeration is to identify all possible entries to the system, not try them out as soon as we find one.
- we map out the internal and external, digital and real infrastructure of target and plan our attack

## Enumeration Principles
1. There is more than meets the eye. Consider all points of view
2. Distinguish between what we see and what we do not see.
3. Always ways to gain more information. Understand the target

Some questions to go over with
- What can we see?
- what reasons can we have for seeing it?
- what image does what we see create for us?
- what do we gain from it?
- how can we use it?
- what can we not see?
- what reasons can there be that we do not see?
- what image results for us from what we do not see?

## Enumeration Methodology
![[Pasted image 20240321233351.png|1125]]

| **Layer**                | **Description**                                                                                        | **Information Categories**                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `1. Internet Presence`   | Identification of internet presence and externally accessible infrastructure.                          | Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures      |
| `2. Gateway`             | Identify the possible security measures to protect the company's external and internal infrastructure. | Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare                  |
| `3. Accessible Services` | Identify accessible interfaces and services that are hosted externally or internally.                  | Service Type, Functionality, Configuration, Port, Version, Interface                               |
| `4. Processes`           | Identify the internal processes, sources, and destinations associated with the services.               | PID, Processed Data, Tasks, Source, Destination                                                    |
| `5. Privileges`          | Identification of the internal permissions and privileges to the accessible services.                  | Groups, Users, Permissions, Restrictions, Environment                                              |
| `6. OS Setup`            | Identification of the internal components and systems setup.                                           | OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files |

1. Internet presence - identify all possible target systems and interfaces that can be tested
2. gateway - understand what we are dealing with and what we have to watch out for (fire walls, etc)
3. Accessible Services - understand the reason and functionality of the target system and gain the necessary knowledge to communicate with it and exploit it for our purposes effectively
4. Processes - understand system processes and identify dependencies between them
5. Privileges - you know
6. OS setup - see how admins manage the system, what internal info we can collect from these behaviors