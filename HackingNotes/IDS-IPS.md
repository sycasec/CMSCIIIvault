# IDS and IPS

## Intrusion Detection System (IDS)
- built for detecting vuln exploits against a target application or computer
- listen only to traffic
- usually a dedicated server connected to a port on a switch that monitors traffic and reports results to admin
- cannot automatically take action to prevent detected exploit
## Intrusion Prevention System
- automatically takes action upon detection of exploit
- statistical and anomaly based
- often positioned directly behind firewall / router / edge device
- actively scans traffic and reports back on threats
- placed inline between source and destination

## Threat Detection
### Signature Based
- check packet signature against database for anomalies
### Anomaly based
- if traffic that doesnt follow protocol is found, an alert is raised
### Host based
- apps that protect computers
- listens to computer received and sent by endpoint
- software
### Networked
- sits in the middle of the traffic listening to traffic stream 
- hardware
