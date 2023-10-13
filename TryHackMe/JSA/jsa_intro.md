
# Junior Security Analyst Intro

```toc
```

## Career as a junior (associate) sec analyst
- triage specialist
	- triaging or monitoring event logs and alerts

### Responsibilities
- monitor and investigate alerts
	- 24x7 SOC (*what is SOC?*) operations environment
- configure and manage security tools 
- develop and implement basic *intrusion detection system* (**IDS**)
- participate in SOC working groups, meetings
- create tickets and escalate the security incidents to the Tier 2 and Team Lead if necessary
### Qualifications
- 0-2 years of experience with **Security Operations** 
- Basic understanding of Networking
	- OSI model
	- TCP/IP model
	- Operating Systems
	- Web Apps
	- scripting/programming is a plus
### Desired Certs
- CompTIA Security+
## Security Operations Center (SOC)
### Core function
- investigate, monitor, prevent, and respond to threats in cyber 24/7
- “SecOps teams are charged with monitoring and protecting many assets”
- SecOps teams act as the central point of collab in coordinated efforts to monitor, assess, and defend against cyber attacks
### Responsibilities
#### PREPARATION AND PREVENTION
- as a JSA, stay informed of current cyber security threats
- gather intelligence data on threats, threat actors, TTPs (Tactics, Techniques, Procedures)
#### MONITORING AND INVESTIGATION
- use **SIEM** ( *Security Information and Event Management* ) and **EDR** ( *Endpoint Detection and Response* ) tools
- prioritise alerts based on threat level:
	- Low
	- Medium
	- High
	- Critical
- JSA perform triaging on the ongoing alerts by exploring and understanding how a certain attack works
	- prevent attacks from happening if they can
	- raise the questions “how, when, and why”

## Day in the Life
### SIEM Dashboard
- **Logs**
	- 07-16-2021 at 05:27:00:347
		- SSH at port 22 from 221.181.185.159
	- 07-16-2021 at 05:25:28
		- Unauthorized connection from 221.181.185.159 to port 22
			- SSH?
	- 07-16-2021 at 02:43:22
		 - user John Doe logged in (Event ID 4624)
	- 07-16-2021 at 02:43:20
		 - multiple failed logins from John Doe
	- 07-16-2021 at 02:43:20
### IP scanner
- 221.181.185.159
- 100% Malicious
- ISP - China Mobile Communications Corporation
- Domain Name - chinamobileltd.thm
- Country - China
- City - Zhenjiang, Jiangsu
### Escalate to Staff Member
- Escalate to SOC team lead Will Griffin
### Flag
- THM{UNTIL-WE-MEET-AGAIN}