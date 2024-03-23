# File Transfer Protocol
```toc
```
## FTP
FTP is one of the oldest protocols on the internet
- runs within application layer of `TCP/IP`
- same layer as `HTTP` or `POP`
- can work with browser or email client support
- has different commands and status codes
	- client side instructs server with several commands
		- upload, download, organize, delete files
	- server responds with a status code after each command
		- [wikipedia status code list](https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes)
- usually **credentials are needed to use FTP on a server**
- FTP is a *clear-text* protocol that can be *sniffed* under certain network conditions
	- some servers offer **anonymous FTP**, though options for users are limited
### FTP connection
- two channels are opened
- first, client and server establish control channel through **`TCP port 21`**
- client sends commands to server, server returns status codes
- both client and server can establish data channel via **`TCP port 20`**
	- exclusively used for data transmission
	- protocol watches for errors during this process
	- if connection broken off during transmission, transport can be resumed after re-establishing contact

### Active vs Passive FTP
**Active**
- client establishes connection via **`TCP port 21`**
- informs server via which client-side port the server can transmit responses
- if a firewall protects client, server cannot reply: all connections are blocked
**Passive**
- server announces a port which the client can establish data channel
- client initiates connection in this method, transfer not blocked by firewall

## TFTP
**Trivial File Transfer Protocol**
- simpler than FTP and performs file transfers between client and server
- *does not* provide user authentication, among other valuable features in FTP
- uses **`UDP`**
	- unreliable protocol due to UDP-assisted application layer recovery
- *does not* support login via passwords 
- sets limits on access based solely on read and write permissions of a file 
- may only be used in local and protected networks
- *does not* have a directory listing functionality
### TFTP commands
| **Commands** | **Description**                                                                                                                        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `connect`    | Sets the remote host, and optionally the port, for file transfers.                                                                     |
| `get`        | Transfers a file or set of files from the remote host to the local host.                                                               |
| `put`        | Transfers a file or set of files from the local host onto the remote host.                                                             |
| `quit`       | Exits tftp.                                                                                                                            |
| `status`     | Shows the current status of tftp, including the current transfer mode (ascii or binary), connection status, time-out value, and so on. |
| `verbose`    | Turns verbose mode, which displays additional information during file transfer, on or off.                                             |
## `vsFTPd` FTP server config
One of the most used FTP servers on `Linux` is **`vsFTPd`**
- default conf found in `/etc/vsftpd.conf`

Here are some of the dangerous config settings that may be allowed 

| **Setting**                    | **Description**                                                                    |
| :----------------------------- | :--------------------------------------------------------------------------------- |
| `anonymous_enable=YES`         | Allowing anonymous login?                                                          |
| `anon_upload_enable=YES`       | Allowing anonymous to upload files?                                                |
| `anon_mkdir_write_enable=YES`  | Allowing anonymous to create new directories?                                      |
| `no_anon_password=YES`         | Do not ask anonymous for password?                                                 |
| `anon_root=/home/username/ftp` | Directory for anonymous.                                                           |
| `write_enable=YES`             | Allow the usage of FTP commands: STOR, DELE, RNFR, RNTO, MKD, RMD, APPE, and SITE? |

As soon as we log in to the FTP server, a `response code 220` is displayed with the banner of the FTP server
- often contains `service` description and `version`

Here is an example of an **anonymous login**
```python
sycasec@htb[/htb]$ ftp 10.129.14.136

Connected to 10.129.14.136.
220 "Welcome to the HTB Academy vsFTP service."
Name (10.129.14.136:cry0l1t3): anonymous

230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.


ftp> ls

200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 1002     1002      8138592 Sep 14 16:54 Calender.pptx
drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Clients
drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Documents
drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Employees
-rw-rw-r--    1 1002     1002           41 Sep 14 16:45 Important Notes.txt
226 Directory send OK.
```

## FTP commands

| **Command**                                                | **Description**                                                                                                                           |
| ---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `ls`                                                       | list directory contents                                                                                                                   |
| `status`                                                   | show overview of FTP server settings                                                                                                      |
| `debug`                                                    | toggles debugging mode                                                                                                                    |
| `trace`                                                    | toggles packet tracing                                                                                                                    |
| `get`                                                      | downloads a specified file                                                                                                                |
| `wget -m -no-passive ftp://<user>:<password>@<ip.address>` | downloads everything available from an FTP server anonymously if anonymous is enabled, replace `<user>` and `<password>` with `anonymous` |
| `put`                                                      | upload a file                                                                                                                             |

## FTP Lab
1. Which version of the FTP server is running on the system? Submit the entire banner as the answer.

I know we dont have to do it, but I went ahead and did an nmap scan anyway
```bash
sudo nmap -sV -A -T4 10.129.203.31 --stats-every=30s
Nmap scan report for 10.129.203.31 (10.129.203.31)
Host is up (0.21s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
| fingerprint-strings:
|   GenericLines:
|     220 InFreight FTP v1.1
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
111/tcp  open  rpcbind     2-4 (RPC #100000)
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
|   100005  1,2,3      43827/tcp6  mountd
|   100005  1,2,3      45101/tcp   mountd
|   100005  1,2,3      53680/udp6  mountd
|   100005  1,2,3      55786/udp   mountd
|   100021  1,3,4      34453/tcp   nlockmgr
|   100021  1,3,4      36249/udp6  nlockmgr
|   100021  1,3,4      40453/tcp6  nlockmgr
|   100021  1,3,4      50168/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 4.6.2
445/tcp  open  netbios-ssn Samba smbd 4.6.2
2049/tcp open  nfs         3-4 (RPC #100003)
```

focusing on the ftp port:
```python
21/tcp   open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
```

Not really sure what that’s supposed to stand for, but I’m guessing `ftpuser` is a username and password. Not sure how nmap figured that out either.

so we do connect via ftp
```python
ftp> open 10.129.203.31
Connected to 10.129.203.31.
ftpuser
220 InFreight FTP v1.1
Name (10.129.203.31:sycasec): 331 Anonymous login ok, send your complete email address as your password
Password:
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
226 Transfer complete
ftp> get flag.txt
200 PORT command successful
150 Opening BINARY mode data connection for flag.txt (39 bytes)
226 Transfer complete
39 bytes received in 0.000124 seconds (307 kbytes/s)
ftp> quit
221 Goodbye.
```

So the first answer we submit is `InFreight FTP v1.1`, it didn’t accept the code, so im guessing the code is not part of the banner.

Now the `flag.txt` file is in my home directory, not sure why. Probably because this is the directory i started `ftp` with. Now we can cat out the contents:
```bash
cat flag.txt
HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}
```
