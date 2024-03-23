# Subnetting Cheat Sheet
```toc
```
## How to make it
- Start with 1, double until you reach 128 (from right to left)
- Subtract top row from 256
- From /32, list CIDR notation (from right to left)
it should look like this:
![[Pasted image 20240321040327.png]]

## How to use it
- Given an IP address: `10.1.1.55/28`
	- locate group size that corresponds to CIDR
	- start from `.0` and increase by group size until the target IP is passed
		- in this example `10.1.1.55` is right between `.48` and `.64`
	- we can now start identifying the 7 attributes of the subnet of target IP
		- `.48` is NetID
		- `.63` is Broadcast
		- Number of IP addresses is 14 (16 - 2, reserved for `NetID` and `BrdID`)
		- Next network is `.64`

### Forrmalized Steps
- Use given CIDR/mask to find column on cheat sheetr
	- each column is a group
	- locate `Group Size`
	- Start at `.0` in the relevant column
	- increase by `Group Size` until target IP is passed
- Number before target IP is Network ID
- Number after target IP is Next Network NetID
- Next Network - 1 = Broadcast
- NetID + 1 = FIrst Host
- Broadcast - 1 = Last Host
- Group Size - 2 = # of usable IP addresses