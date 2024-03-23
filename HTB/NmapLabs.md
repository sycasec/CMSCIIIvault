# Firewall IDS/IPS Labs
## Easy
A company hired us to test their IT security defenses, including their `IDS` and `IPS` systems. Our client wants to increase their IT security and will, therefore, make specific improvements to their `IDS/IPS` systems after each successful test. We do not know, however, according to which guidelines these changes will be made. Our goal is to find out specific information from the given situations.

We are only ever provided with a machine protected by `IDS/IPS` systems and can be tested. For learning purposes and to get a feel for how `IDS/IPS` can behave, we have access to a status web page at: `http://<target>/status.php`

This page shows us the number of alerts. We know that if we receive a specific amount of alerts, we will be `banned`. Therefore we have to test the target system as `quietly` as possible.

```python
nmap 10.129.85.152 --script smb-os-discovery
Nmap scan report for 10.129.85.152 (10.129.85.152)
Host is up (0.27s latency).
Not shown: 869 closed tcp ports (conn-refused), 128 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
10001/tcp open  scp-config
```

```python 

```



| Mask | Network Addr   | Next Hop       | Interface |
| ---- | -------------- | -------------- | --------- |
| /26  | 192.168.23.0   | -              | m0        |
| /27  | 192.168.23.64  | -              | m2        |
| /28  | 192.168.23.96  | -              | m3        |
| /29  | 192.168.23.112 | -              | m4        |
| /30  | 192.168.23.120 | -              | m5        |
| /30  | 192.168.1.1    | 192.168.23.121 | m5        |
| /any | any            | 192.168.23.121 | m5        |
