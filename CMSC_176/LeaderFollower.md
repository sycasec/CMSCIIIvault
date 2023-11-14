
[[CMSC_176root]]

```toc
```

# Design and Implementation of a Leader-Follower Smart Office Lighting Control System Based on IoT Technology

## Short Background
- Lighting systems have outdated and poor energy efficiency
- urgent need for smart LED lighting system that are:
	- energy efficient
	- convenient to install
	- inexpsensive
- Original literature is Wireless Sensor Networks
	- more efficient than wired networks because they are easier to implement
	- other examples are smart LED streetlights
		- where daylight and artificial light can be measured and recorded through sensors
			- this is used to regulate the WSN LED lighting
	- problem with existing systems is they are usually costly to install
		- used in simple spaces like toilets and corridors
		- not used in complex spaces such as offices

## Related works
### Tech
- Applicable fields include
	- Living Room
	- Street
	- Indoor
	- Classroom
	- Public Space
- Sensors include
	- smartphone camera
	- PIR Sensor (passive infrared)

## Proposed System
### Leader Follower System 
- when the system’s counter is zero and the PIR sensors cannot detect people:
	- all indoor LED lights go to *low-light mode*
	- power consumption of low light is 1/10 of *high-light* mode 
- Parameters for the lighting system can be adjusted via internet
	- **Duration** of high-light mode
	- **Power** of high-light mode
	- **Power** of low-light mode
### Energy Savings Calculation and Discussion
- Factors that affect power consumption are measured:
	- duration of high-light $T$
	- power of high-light mode $W_H$
	- power of low-light mode $W_L$
	- pr 