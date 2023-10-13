[[CMSC137_root]]

# Lecture 2

```toc
```

# Network Topology

## Physical Topology
- way in which a network is laid out physically
## Network Topology
- geometric representation of the relationship of all the **links and linking devices** (nodes) to one another
- four basic toplogies:
	- **mesh**
	- **star**
	- **bus**
	- **ring**
	- line or point-to-point
	- tree
	- hybrid

### Mesh topology
- #### Fully Connected Mesh
	- every device has a dedicated p2p link to every other device
	- physical links: n (n-1)
	- duplex mode: n (n-1) / 2
	- **Disadvantages**
		- high amount of cabling and I/O ports
		- difficult installation and reconnection
		- wiring bulk
		- expensive hardware
	- **Advantages**
		- Eliminates traffic problems
		- robust
		- privacy / sec
		- easy fault identification and fault isolation
- #### Partially Connected Mesh
	- at least two of the computers in the network have connections to multiple other computers in the network
### Star Topology
- used in local area networks (LANs)
- each device has a dedicated p2p link only to a central controller (hub)
- devices are not directly linked to one another 
- controller acts as an exchange
- #### Disadvantages
	- Dependency on a single point
	- more cabling than ring or bus topology
- #### Advantages
	- less expensive than mesh
	- need only one link and one IO port for connection to all
	- easy to install and config
	- additions, moves and deletions involve one connection
	- robust
	- easy fault identification and isolation
### Bus Topology
- used to be popular for ethernet lans 
- multipoint
- one long cable links all devices in a network
- nodes are connected to the bus cable via:
	- *droplines* - connection running between the device and main cable
	- *taps* - connector that splices into main cable or just forcefully inserted
- #### Disadvantages
	- Limited number of taps and distance between taps
	- Difficult reconnection and fault isolation
	- difficult to add new devices
	- signal reflection at taps can cause quality degradation
		- also affected by number of taps and spacing
	- fault or break in bus cable stops all transmission
- #### Advantages
	- Easy to install (???)
	- less cabling 
### Ring Topology
- each device has a dedicated p2p with the only two devices adjacent to it
- signal is passed along the ring in one direction in each node until destination
- each device in the ring incorporates a repeater
- #### Disadvantages 
	- a break in ring can disable the entire network. (solved by dual ring) 
- #### Advantages 
	- relatively easy to install
	- simplified fault isolation
### Tree Topology
- starbus (coffee)
- central nodes or star networks are connected
	- router to router (hub2hub)?
- hierarchy
### Hybrid
- 