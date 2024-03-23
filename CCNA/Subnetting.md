# Subnetting
- Taking a network and dividing it into smaller sub-networks

lets say we have a `10.0.0.x/24` network, we can break that down into two `10.0.0.x/25` networks

## Seven Attributes of a Subnet 
using this example 
![[Pasted image 20240321035248.png|328]]
### Network ID
- first possible address in each subnet 
- in the `/25` network, the *Network ID* is `10.0.0.0`
- used to identify a specific subnet
	- cannot be assigned to user
	- No. if IPs = 128
	- Usable IPs = 126 (Net ID and Broadcast IP reserved)
- if we say `10.0.0.0/24` it refers to the entire network
	- since `/24` is for `256` addresses
- If we say `10.0.0.0/25` it refers to just the first subnet
### Broadcast IP
- last possible address in each subnet
- cannot be assigned to user 
- allows user to speak to every other IP in the subnet
	- send a packet to `10.0.0.127` and it will be broadcast to the entire subnet
### First Host IP
- since our `NetID` is `10.0.0.0`
- our first host `ip` is `10.0.0.1`
### Last Host IP
- since our `Broadcast IP` is `10.0.0.127`
- our last host IP is `10.0.0.126`
### Next Network
- the IP address right after the broadcast address
### No. of IP addresses
- amount of addresses in a subnet
### CIDR/Subnet
- subnet mask
- indicates the total size / total amount of addresses in the subnet 


