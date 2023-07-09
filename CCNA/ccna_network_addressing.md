# Network Layer Addressing and Subnetting

## Intro to IP Addressing
- `203.0.113.10`
- `203.0.113` **NETWORK**
- `.10` *HOST*

### Classless Addressing
#### SUBNET MASK
- in the example, `203.0.113.10`
- network is represented in bin as `11001011.00000000.01110001.00001010`
- subnet mask represents net and host as ones and zeros respectively
	- `11111111.11111111.11111111.00000000`
	-                network                     host

### IP address types
- #### network address
	- group of devices with network prefix
	- 0 in the host portion `203.0.113.0`
- #### broadcast address
	- all devices on a network
	- 255 in the host portion `203.0.113.255`
- #### host address
	- unique devices on a network
	- in between 0 and 255 in the host portion