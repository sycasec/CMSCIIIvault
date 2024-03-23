---
date_created: 2024-03-05
date_modified: 2024-03-05
type: pentester_notes
entry number: "3"
topic: Firewall and IDS/IPS Evasion
---

```toc
```

# Firewall and IDS/IPS Evasion
## Firewalls
**Nmap** gives us many ways to bypass firewalls rules and IDS/IPS

Firewall is a security measure against unauthorized connection attempts from external networks
Based on a software component that:
- monitors network traffic between the firewall and incoming data connections
- Decide how to handle connections based on a ruleset
Checks whether individual network packets are being passed, ignored, or blocked

## IDS/IPS
- Intrusion Detection System (**`IDS`**)
- Intrusion Prevention System (**`IPS`**)
- software based components
- scans network for potential attacks
	- analyze and report attacks
- **`IPS`** complements **`IDS`** by taking specific defensive measures if potential attack has been detected
- analysis based on pattern matching and signatures
- if a service detection scan is detected, `IPS` can prevent pending connection attempts
----
### Determine Firewalls and Their Rules
- if a port is shown as filtered, it was *dropped* or *rejected*
- dropped packets are ignored and no response from host
- rejected packets are returned with `RST` flag
	- may contain nothing at all, or any of these error codes:
	- `Net Unreachable`
	- `Net Prohibited`
	- `Host Unreachable`
	- `Host Prohibited`
	- `Port Unreachable`
	- `Proto Unreachable`

`Nmap`’s `TCP ACK scan (-sA)` method is much harder to filter for firewalls and `IDS/IPS` systems than:
- regular `SYN (-sS)`
- Connect scans `-sT`
because they only send a`TCP` packet with only the `ACK` flag.

 - When a port is closed or open, host must respond with **`RST`** flag
 - All connection attempts with **`SYN`** flag from external networks are usually blocked by firewalls
 - packets with **`ACK`** flag are passed because firewall cannot determine whether the connection was first established from external or internal network

## Detect IDS/IPS
- much more difficult because these are passive traffic monitoring systems
- **`IDS systems`** examine all connections between hosts
	- if `IDS` finds packets containing defined contents or specifications, admin is notified
- **`IPS systems`** take measures configured by admin independently to prevent potential attacks automatically
- Several virtual private servers **`VPS`** with different IP addresses are recommended to determine whether such systems are on the target network during a pentest
	- If admin detects potential attack on target network, IP block is imminent
	- ISP maybe contacted blocking us access to internet

## Decoys
- to avoid getting blocked by IPS, use decoy scanning **-D**
- nmap generates various random IP addresses inserted into the IP header to disguise origin of packet sent
	- generate a random N amount of IP addresses
### Scan using Decoy

```python
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p 80 -sS -Pn -n --disable-arp-ping --packet-trace -D RND:5

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-21 16:14 CEST
SENT (0.0378s) TCP 102.52.161.59:59289 > 10.129.2.28:80 S ttl=42 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
SENT (0.0378s) TCP 10.10.14.2:59289 > 10.129.2.28:80 S ttl=59 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
SENT (0.0379s) TCP 210.120.38.29:59289 > 10.129.2.28:80 S ttl=37 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
SENT (0.0379s) TCP 191.6.64.171:59289 > 10.129.2.28:80 S ttl=38 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
SENT (0.0379s) TCP 184.178.194.209:59289 > 10.129.2.28:80 S ttl=39 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
SENT (0.0379s) TCP 43.21.121.33:59289 > 10.129.2.28:80 S ttl=55 id=29822 iplen=44  seq=3687542010 win=1024 <mss 1460>
RCVD (0.1370s) TCP 10.129.2.28:80 > 10.10.14.2:59289 SA ttl=64 id=0 iplen=44  seq=4056111701 win=64240 <mss 1460>
Nmap scan report for 10.129.2.28
Host is up (0.099s latency).

PORT   STATE SERVICE
80/tcp open  http
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.15 seconds
```

The spoofed packets are often filtered out by ISPs and routers though. 
We can also specify our VPS server’s IP addresses and use them in combination with **`IP ID`**

### Scan using different source IP
| **Scanning Options** | **Description**                                        |
| -------------------- | ------------------------------------------------------ |
| `10.129.2.28`        | Scans the specified target.                            |
| `-n`                 | Disables DNS resolution.                               |
| `-Pn`                | Disables ICMP Echo requests.                           |
| `-p 445`             | Scans only the specified ports.                        |
| `-O`                 | Performs operation system detection scan.              |
| `-S`                 | Scans the target by using different source IP address. |
| `10.129.2.200`       | Specifies the source IP address.                       |
| `-e tun0`            | Sends all requests through the specified interface.    |
```python
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -n -Pn -p 445 -O -S 10.129.2.200 -e tun0

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-22 01:16 CEST
Nmap scan report for 10.129.2.28
Host is up (0.010s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (96%), Linux 3.2 - 4.9 (96%), Linux 2.6.32 - 3.10 (96%), Linux 3.4 - 3.10 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Synology DiskStation Manager 5.2-5644 (94%), Linux 2.6.32 - 2.6.35 (94%), Linux 2.6.32 - 3.5 (94%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 4.11 seconds
```
## DNS proxying
- by default, reverse DNS resolution is done unless specified otherwise
- DNS queries passed in most cases because the given web server is supposed to be found
- queries are made over the **`UDP port 53`**
- **`TCP Port 53`** was previously only used for **`Zone Transfers`** between DNS servers or data transfer larger than 512 bytes
	- this is changing due to `IPv6` and `DNSSEC` expansions
	- `DNS` requests can be made via **`TCP Port 53`**
- we can use **`TCP Port 53`** as a source port **`--source-port`** 
	- if admin does not filter `IDS`/`IPS` properly, `TCP` packets should be trusted
### Filtered Scan
```python
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-21 22:50 CEST
SENT (0.0417s) TCP 10.10.14.2:33436 > 10.129.2.28:50000 S ttl=41 id=21939 iplen=44  seq=736533153 win=1024 <mss 1460>
SENT (1.0481s) TCP 10.10.14.2:33437 > 10.129.2.28:50000 S ttl=46 id=6446 iplen=44  seq=736598688 win=1024 <mss 1460>
Nmap scan report for 10.129.2.28
Host is up.

PORT      STATE    SERVICE
50000/tcp filtered ibm-db2

Nmap done: 1 IP address (1 host up) scanned in 2.06 seconds
```

### SYN-scan from DNS port (53)
```python
sycasec@htb[/htb]$ sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace --source-port 53

SENT (0.0482s) TCP 10.10.14.2:53 > 10.129.2.28:50000 S ttl=58 id=27470 iplen=44  seq=4003923435 win=1024 <mss 1460>
RCVD (0.0608s) TCP 10.129.2.28:50000 > 10.10.14.2:53 SA ttl=64 id=0 iplen=44  seq=540635485 win=64240 <mss 1460>
Nmap scan report for 10.129.2.28
Host is up (0.013s latency).

PORT      STATE SERVICE
50000/tcp open  ibm-db2
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
```

