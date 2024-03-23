---
date_created: 2024-02-19
date_modified: 2024-02-21
type: pentester_notes
entry number: "2"
topic: Host and Port Scanning
---

# Host and Port Scanning
- to get a more accurate picture of the system, we need:
	- Open ports and services
	- Service versions
	- Information that the services provided
	- Host OS

- there are 6 states for each scanned port

| State | Description |
| ---: | :--- |
| `open` | This indicates that the connection to the scanned port has been established. These connections can be **TCP connections**, **UDP datagrams** as well as **SCTP associations**. |
| `closed` | When the port is shown as closed, the TCP protocol indicates that the packet we received back contains an `RST` flag. This scanning method can also be used to determine if our target is alive or not. |
| `filtered` | no response or error code returned from target |
| `unfiltered` | only occurs during **`TCP-ACK`** scan – port is accessible, cannot be determined if open or closed |
| `open\|filtered` | if no response from port, Nmap sets this state – may be an indication of firewall or packet filter protecting port |
| `closed\|filtered` | only occurs on **`IP ID idle`** scans – impossible to determine if closed or filtered |

## Discovering Open TCP Ports
- `nmap` scans top 1000 `TCP` ports with `SYN` scan (`-sS`)
- default when run as `root`
	- root privilege required to create raw `tcp` packets
	- otherwise, `TCP` scan is performed (`-sT`)
- we can define ports by:
	- individually
	- range
	- top ports (**`--top-ports=10`**)
	- scan all ports (**`-p-`**)
	- fast port scan of top 100 ports **(`-F`)**
### Scanning top 10 `tcp` ports
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 --top-ports=10 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:36 CEST
Nmap scan report for 10.129.2.28
Host is up (0.021s latency).

PORT     STATE    SERVICE
21/tcp   closed   ftp
22/tcp   open     ssh
23/tcp   closed   telnet
25/tcp   open     smtp
80/tcp   open     http
110/tcp  open     pop3
139/tcp  filtered netbios-ssn
443/tcp  closed   https
445/tcp  filtered microsoft-ds
3389/tcp closed   ms-wbt-server
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 1.44 seconds
```
### Nmap packet trace
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p 21 --packet-trace -Pn -n --disable-arp-ping

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:39 CEST
SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 S ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 RA ttl=64 id=0 iplen=40  seq=0 win=0
Nmap scan report for 10.11.1.28
Host is up (0.014s latency).

PORT   STATE  SERVICE
21/tcp closed ftp
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

| **Scanning Options** | **Description** |
| :--- | :--- |
| `10.129.2.28` | Scans the specified target. |
| `-p 21` | Scans only the specified port. |
| `--packet-trace` | Shows all packets sent and received. |
| `-n` | Disables DNS resolution. |
| `--disable-arp-ping` | Disables ARP ping. |
- `line 4`: we sent `TCP` packet with `SYN` flag **(`S`)** to target `10.129.2.28`at port 63090
- `line 5`: `RCVD` a `TCP` packet response containing **`RST`** and **`ACK`** flags **(`RA`)**
	- `RST` - end `TCP` session
	- `ACK` - acknowledge `TCP` packet

### Connect Scan
Nmap TCP Connect Scan **`-sT`** uses TCP three-way handshake to determine if a specific port on a target host is open or closed
- considered open if port responds with `SYN-ACK (SA)`
- closed if `RST` response packet

The **Connect** scan is the most accurate and stealthy way to determine state of a port.
- *no unfinished connections* or unsent packets
- *less likely to be detected* by intrusion prevention / detection systems (IPS/IDS)
- useful to map network *without* disturbing running services
- can *bypass firewall* and accurately determine state of target ports
- *slower* than other types of scan
	- requires scanner to wait for a response after each packet it sends
	- could take some time if target is busy or unresponsive

#### Sample Connect Scan
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p 443 --packet-trace --disable-arp-ping -Pn -n --reason -sT 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:26 CET
CONN (0.0385s) TCP localhost > 10.129.2.28:443 => Operation now in progress
CONN (0.0396s) TCP localhost > 10.129.2.28:443 => Connected
Nmap scan report for 10.129.2.28
Host is up, received user-set (0.013s latency).

PORT    STATE SERVICE REASON
443/tcp open  https   syn-ack

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
```

### Filtered Ports
In most cases, firewalls have rulesets to handle specific connections
- packets can either be **dropped** or **rejected**

By default, nmap retries to send the packet once, determined by the `--max-retries=1` default.
lets look at an example where the **firewall** `TCP` packets we send for port scan
- scan `TCP` on port 139 (filtered)
- deactivate `ICMP Echo Requests` with **`-Pn`** to track how sent packets are handled
- DNS resolution `-n`
- disable `ARP` ping `--disable-arp-ping`
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p 139 --packet-trace -n --disable-arp-ping -Pn

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:45 CEST
SENT (0.0381s) TCP 10.10.14.2:60277 > 10.129.2.28:139 S ttl=47 id=14523 iplen=44  seq=4175236769 win=1024 <mss 1460>
SENT (1.0411s) TCP 10.10.14.2:60278 > 10.129.2.28:139 S ttl=45 id=7372 iplen=44  seq=4175171232 win=1024 <mss 1460>
Nmap scan report for 10.129.2.28
Host is up.

PORT    STATE    SERVICE
139/tcp filtered netbios-ssn
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 2.06 seconds
```

|**Scanning Options**|**Description**|
|---|---|
|`10.129.2.28`|Scans the specified target.|
|`-p 139`|Scans only the specified port.|
|`--packet-trace`|Shows all packets sent and received.|
|`-n`|Disables DNS resolution.|
|`--disable-arp-ping`|Disables ARP ping.|
|`-Pn`|Disables ICMP Echo requests.|

### Discovering Open `UDP` ports 
Some sysadmins forget to filter `UDP` in addition to `TCP`
- `UDP` is a *stateless protocol*
- does not require 3-way handshake like `TCP`
- we do not receive `ACK`
- `UDPO scan` **`-sU`** slower than `TCP scan` **`-sS`** because timeout is much longer
#### Sample UDP port scan 
```shell-session
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -F -sU

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 16:01 CEST
Nmap scan report for 10.129.2.28
Host is up (0.059s latency).
Not shown: 95 closed ports
PORT     STATE         SERVICE
68/udp   open|filtered dhcpc
137/udp  open          netbios-ns
138/udp  open|filtered netbios-dgm
631/udp  open|filtered ipp
5353/udp open          zeroconf
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 98.07 seconds
```

| **Scanning Options** |**Description**|
|---|---|
|`10.129.2.28`|Scans the specified target.|
|`-F`|Scans top 100 ports.|
|`-sU`|Performs a UDP scan.|
