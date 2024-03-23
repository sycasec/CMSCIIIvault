---
date_created: 2024-02-18
date_modified: 2024-02-19
type: pentester_notes
entry number: "1"
topic: network enumeration with nmap
---
# Enumeration
- critical part of pentesting
- identify all the ways a target could be attacked
- imagine the following situation
> Our partner is not at home and has misplaced our car keys. We call our partner and ask where the keys are. If we get an answer like “in the living room”, it is entirely unclear and can take much time to find them there. However, if our partner tells us that something like “in the living room on the white shelf, next to the TV, in the third drawer” - it will be much easier to find them

- In a similar note, its not hard to get access to the target system once we know how to do it. We can narrow this down with:
	- **Functions or resources that allow us to interact with the target and/or provide additional information**
	- **information that provides us with more important information**
- **Manual enumeration is critical component**

```toc
```
## Nmap Architecture
scanning techniques:
- host discovery
- port scanning
- service enumeration and detection
- OS detection
- Scriptable interaction with target service (nmap scripting engine)
### Syntax 
`$ nmap <scan types> <options> <target>`

### Scan Techniques
```shell-session
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
```
- **`TCP/SYN`** scan (**`-sS`**) default, most popular, scans several thousand ports per second
	- sends one packet with **`SYN`** flag, never completes 3 way handshake, no full `TCP` connection established
	- if target sends **`SYN-ACK`** packet back to scanned port, nmap detects this port is **`open`**
	- if **`RST`** flag is received, port is **`closed`**
	- if no packet, displayed as **`filtered`**
		- certain packets may be dropped/ignored by firewall

## Host Discovery
- for pentest of network or company, use host discovery methods
- most effective is **ICMP echo requests**
- store every single scan for comparison, documentation, reporting
### Scan network range
example scan:
```shell-session
sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5
```

| Scanning Options | Description |
| ---- | ---- |
| 10.129.2.0/24 | Target Network Range |
| -sn | Disables Port Scanning |
| -oA tnet | stores results in all formats starting with the name ‘tnet’ |
- this scanning method only works of the host firewall allows it
- will be discussed in Firewall and IDS Evasion

### Scan IP List
- nmap gives the option of working with lists and reading hosts from lists
	- the previous filed stored with the name `tnet` - in that exact format
- we can also input the ips to scan right after the scan type
	- `sudo nmap -sn -oA tnet 10.129.2.18 10.129.2.19 10.129.2.20`
- or ip range
	- `sudo nmap -sn -oA tnet 10.129.2.18-20`
- by disabling port scan (`-sn`) nmap automatically ping scan with **`ICMP Echo Requests`** (**`-PE`**)
	- if this request is sent we expect an **`ICMP reply`** if the pinging host is alive
	- our previous scans sent an **`ARP` ping** resulting in **`ARP` replies**.
### Scan Host

- to ensure that **`ICMP Echo`** requests are sent, we pass the parameter **`-PE`**
- we can confirm our packet sent and received with **`--packet-trace**
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:08 CEST
SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.2
RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
Nmap scan report for 10.129.2.18
Host is up, received arp-response (0.023s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```

| Scanning Options | Description |
| :--- | :--- |
| `10.129.2.18` | Scan target host |
| `-sn` | Disables Port Scanning |
| `-oA host` | stores results in all formats starting with the name ‘host’ |
| `-PE` | ping scan with `ICMP Echo requests` |
| `--packet-trace` | show all packets sent and received |
| `--reason` | displays reason for specific result |

- nmap can detect whether host is alive or not through **`ARP request` & `ARP reply`** 
- to disable `ARP request`, **`--disable-arp-ping**
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace --disable-arp-ping 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:12 CEST
SENT (0.0107s) ICMP [10.10.14.2 > 10.129.2.18 Echo request (type=8/code=0) id=13607 seq=0] IP [ttl=255 id=23541 iplen=28 ]
RCVD (0.0152s) ICMP [10.129.2.18 > 10.10.14.2 Echo reply (type=0/code=0) id=13607 seq=0] IP [ttl=128 id=40622 iplen=28 ]
Nmap scan report for 10.129.2.18
Host is up (0.086s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
```
