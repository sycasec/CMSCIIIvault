# Network File System
## What is `NFS`
- developed by Sun Microsystems
- same purpose as `SMB`, but entirely different protocol
- used between `Linux` and `Unix` systems
- internet standard that governs procedures in a distributed file system
- `NFS Protocol v3.0 (NFSv3)` authenticates client computer
- `NFS Protocol v4.0 (NFSv4)` user must authenticate (similar to `SMB`)

`NFSv4` uses either `UDP` or `TCP` port **`2049`** to run the service
- based on the *Open Network Computing Remote Procude Call* `(ONC-RPC/SUN-RPC)` 
- exposed on `TCP` and `UDP` ports 111
- uses *External Data Representation* `(XDR)` for system independent data exchange
- no authentication / authorization, shifted to `RPC`' protocol’s options
- most common authentication is via UNIX `UID/GID` and `group memberships`
- 

surprise version table

| **Version** | **Features**                                                                                                                                                                                                                                                         |
| ----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NFSv2`     | It is older but is supported by many systems and was initially operated entirely over UDP.                                                                                                                                                                           |
| `NFSv3`     | It has more features, including variable file size and better error reporting, but is not fully compatible with NFSv2 clients.                                                                                                                                       |
| `NFSv4`     | It includes Kerberos, works through firewalls and on the Internet, no longer requires portmappers, supports ACLs, applies state-based operations, and provides performance improvements and high security. It is also the first version to have a stateful protocol. |
|             |                                                                                                                                                                                                                                                                      |
## Footprinting `NFS` 
### `Nmap`
- blast ports `-p111,2049 -sV -sC`
- also run all `nfs` scripts `--script nfs*`
- literal example
```bash
sudo nmap --script nfs* 10.129.14.128 -sV -p111,2049
```

### Show available `NFS` shares and mount them
`showmount -e <ip.addr>`
- this will show you the available nfs dirs
```bash
mkdir target-nfs
sudo mount -t nfs <ip.addr>:/ ./target-nfs -o nolock
cd target-nfs
tree ./
```

this should show you the dir structure 

## Lab

This one was pretty easy, just do the nmap scan, provides us with this:
```python
❯ sudo nmap --script nfs-ls,nfs-showmount,nfs-statfs 10.129.1.168 -sV -T4 -p111,2049 --stats-every=30s
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-23 01:03 +08
Nmap scan report for 10.129.1.168 (10.129.1.168)
Host is up (1.1s latency).

PORT     STATE SERVICE VERSION
111/tcp  open  rpcbind 2-4 (RPC #100000)
| nfs-ls: Volume /var/nfs
|   access: Read Lookup Modify Extend Delete NoExecute
| PERMISSION  UID    GID    SIZE  TIME                 FILENAME
| rwxr-xr-x   65534  65534  4096  2021-11-08T15:08:27  .
| ??????????  ?      ?      ?     ?                    ..
| rw-r--r--   65534  65534  39    2021-11-08T15:08:27  flag.txt
|_
| nfs-showmount:
|   /var/nfs 10.0.0.0/8
|_  /mnt/nfsshare 10.0.0.0/8
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      40043/tcp   mountd
|   100005  1,2,3      40964/udp   mountd
|   100005  1,2,3      46691/udp6  mountd
|   100005  1,2,3      50901/tcp6  mountd
|   100021  1,3,4      38125/udp6  nlockmgr
|   100021  1,3,4      38467/tcp   nlockmgr
|   100021  1,3,4      41833/udp   nlockmgr
|   100021  1,3,4      43723/tcp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs     3-4 (RPC #100003)
```

Truth is you really didnt need the nmap scan, just `nfs-utils` if you dont have it.
Follow the mounting steps and cat out flag. Actually for some reason, the `nmap script` `nfs-ls` doesn’t show the `mnt/nfsshare`. But that’s it, lab over.