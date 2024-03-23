# Server Message Block
```toc
```
## What is `SMB`?
- a client-server protocol that regulates access file, directory, and other network resources such as printers, routers, and other interfaces
- first became publicly available as part of the `OS/2` network operating system LAN manager and LAN server.
- since then, its main application area has been with Windows operating systems
	- its network services support `SMB` in a downwards compatible manner
	- free software `Samba` enables `SMB` in `Linux` and `Unix` distributions


The `SMB` protocol enables communication, file, and service access between participants in the same network
- to use `SMB`, participants must first have a network protocol and establish connection via `TCP`

Access rights are defined by **`Access Control Lists (ACL`**, giving attributes such as:
- execute
- read
- full access
for individual users or user groups. These are also defined based on shares and do not correspond to the rights assigned locally on the server 
## Samba
- implements the **`Common Internet File System (CIFS)`** protocol
	- created by microsoft
	- Allows samba to communicate with newer windows systems
	- usually referred to as `SMB/CIFS` (wow, what a `stallman` moment)
- Samba usually connects via `TCP` ports:
	- 137
	- 138
	- 139
- `CIFS` uses `TCP` port 445 only
- each host participates in the same `workgroup`
	- `workgroup` identifies arbitrary collection of computers and their resources on the `SMB` network
	- there can be multiple `workgroups` on the network at the same time
- **`IBM`** (yikes) developed an API for networking computers called NetBIOS, providing a blueprint for data sharing in a network
	- when a machine goes online, it gets a name through `name registration` procedure
	- Either each host reserves its hostname on the network
	- or the `NetBIOS Name Server` provides one
	- 

surprise version table of `SMB`

| **SMB Version** | **Supported**                       | **Features**                                                           |
| --------------- | :---------------------------------- | :--------------------------------------------------------------------- |
| CIFS            | Windows NT 4.0                      | Communication via NetBIOS interface                                    |
| SMB 1.0         | Windows 2000                        | Direct connection via TCP                                              |
| SMB 2.0         | Windows Vista, Windows Server 2008  | Performance upgrades, improved message signing, caching feature        |
| SMB 2.1         | Windows 7, Windows Server 2008 R2   | Locking mechanisms                                                     |
| SMB 3.0         | Windows 8, Windows Server 2012      | Multichannel connections, end-to-end encryption, remote storage access |
| SMB 3.0.2       | Windows 8.1, Windows Server 2012 R2 |                                                                        |
| SMB 3.1.1       | Windows 10, Windows Server 2016     | Integrity checking, AES-128 encryption                                 |

Version 4 of `Samba` now provides `daemons` (yikes) along with the `NetBIOS message block daemon (nmbd)` 

## Footprinting SMB
`rpcclient` requests for SMB server

| **Query**                 | **Description**                                                    |
| ------------------------- | :----------------------------------------------------------------- |
| `srvinfo`                 | Server information.                                                |
| `enumdomains`             | Enumerate all domains that are deployed in the network.            |
| `querydominfo`            | Provides domain, server, and user information of deployed domains. |
| `netshareenumall`         | Enumerates all available shares.                                   |
| `netsharegetinfo <share>` | Provides information about a specific share.                       |
| `enumdomusers`            | Enumerates all domain users.                                       |
| `queryuser <RID>`         | Provides information about a specific user.                        |
### Brute Forcing User RIDs
```bash
for i in $(seq 500 1100);do rpcclient -N -U "" 10.129.14.128 -c "queryuser 0x$(printf '%x\n' $i)" | grep "User Name\|user_rid\|group_rid" && echo "";done
```


## Lab

Idk bro i winged it so much

The useful tools are:
- `smbclient`
- `rpcclient`
- `enum4linux-ng` [link to repo](https://github.com/cddmp/enum4linux-ng)
	- not in aur
