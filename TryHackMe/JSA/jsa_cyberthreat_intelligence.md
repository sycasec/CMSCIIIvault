
# Cyber Threat Intelligence

## Cyber Threat Intelligence
- CTI can be defined as evidence based knowledge about adversaries
- *DATA*
	- discrete indicators associated with an adversary
		- IP addresses
		- URLS
		- Hashes
- *INFORMATION*
	- combination of multiple data points
	- how many times have employees accessed tryhackme.com within the month?
		- you will want to check for IP address connections
- *INTELLIGENCE*
	- correlation of data and info to extract patterns of actions based on contextual analysis 
- Primary Goal is to understand your environment, your adversary, and what steps to take for defense
- answer the following questions:
	- who’s attacking you?
	- what are their motivations?
	- what are their capabilities?
	- what artefacts and indicators of compromise should you look out for?
### threat intelligence can be gathered under following categories:
- **Internal**
	- corporate sec events
		- vulnerability assessments
	- cyber awareness training reports
	- system logs and events
- **Community**
	- open web forums
	- dark web communities
- **External**
	- Threat intel feeds
	- online marketplaces
	- public sources
### Threat intelligence classifications
- Strategic Intel
	- High level intel that looks into the organisations’s threat landscape
	- map out risk areas based on trends and patterns
- Technical Intel
	- evidence and artefacts used by adversary
- Tactical
	- adversary’s TTPs
- Operational
	- adversary’s specific motives, allowing secops to identify and narrow down target

## CTI Lifecycle
### Direction
- identify the following parameters
	- information assets and business processes that need protection
	- potential impact in event of losses or process interruptions
	- data sources to be used for protection
	- tools and resources that are required for asset defense
### Collection
- gather data using commercial, private, and open-source resources
- recommended to automate this process
### Processing
- Raw logs, vuln info, malware and network traffic come in different formats when disconnected
- this phase ensures that dat is extracted, sorted, organised, correlated with appropriate tags 
### Analysis
- derive insights from info
	- investigate potetnial threat based on indicators and attack patterns
	- define action plan to avert attack
	- strengthen sec controls
### Dissemination
- inform the managers

## CTI standards and frameworks
### MITRE ATT&CK
- [[https://tryhackme.com/room/mitre]]
- knowledge base of adversary behavior
### TAXII
- *Trusted Automated eXchange of Indicator Information*
- protocols for secure exchange of threat intel for real time detection, prevention, and mitigation
-