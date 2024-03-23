# Network Address Translation
- masks internal system IP address to a public IP address
- handles routing
- method of remapping one IP address space into another by modifying info in IP datagram packet headers while in transit
- additional layer of security
- allows IP of an organization to appear from the outside to use a different address space than what it is exactly using
- allows IP address of network to become a globally routable address space (through translation)
- typically **1 (one)** internet-routable IP address of a NAT gateway is used for an entire private network

## Types
### Static
- one-to-one mapping between local and global address
### Dynamic
- maps unregistered IP to registered IP from a pool of registered IP 
### Overloading
- map multiple unregistered IP to a single public IP when leaving local network
- assigns unique layer 4 (ipv4) source for each IP address it masks
- also known as **Port Address Translation** (PAT)
- thousands of users can be connected to internet by using only one real global IP address