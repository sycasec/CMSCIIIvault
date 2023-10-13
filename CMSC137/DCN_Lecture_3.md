```toc
```

# The Physical Layer

- Based on OSI model 
- 1957 by ISO (International Standards Organization)
- dominated data comms and networking literature before 1990 (replaced by TCP/IP)
- show how to facilitate comms between systems without requiring changes to the logic of underlying hardware and software
- allows comms for all types of computer systems
- coordinates functions required to carry a bit stream over physical medium
- deals with mechanical and electrical specs of the interface and transmission medium
- defines the procedures and functions that physical devices and interfaces have to perform for transmission to occur

## The PL is concerned with 
- physical characteristics of interfaces and medium
- representation of bits for transmission
- data rate
- synchronisation of bits
- line config
- physical topology
- transmission mode

## Theoretical Basis
### Analog and Digital
- analog data
	- refers to info that is continuous
	- infinite number of values in a range
- digital data
	- refers to info that has discrete states
	- limited number of values
### Periodic and !Periodic
- completes a pattern within a measureable time frame called a period
- repeats pattern over identical periods
- completion of a full pattern is called a cycle
- simple periodic analog
	- sine wave cannot be decomposed into simpler signals
- composite periodic analog
	- composed of multiple sine waves
### Sine Wave
- the most fundamental form of a periodic signal
- consists of a single arc above the time axis
- three parameters
	- peak amplitude
	- frequency
	- phase
#### peak amplitude
- absolute value of highest intensity
#### period and frequency
- **period** - time in seconds a signal needs to complete 1 cycle
- **frequency** - number of periods in 1 second
- $T=\frac{1}{f}$

![[Pasted image 20230926204416.png|600]]

### Frequency
- rate of change with respect to time
- change in a short span of time means high frequency
- change over a long span of time means low frequency
## Phase
- position of waveform relative to time 0
- shifted backward or forward
- measured in degrees or radians ($1\degree \equiv \frac{2\pi}{360\degree rad}$ )
- phase shift of $360\degree$ = shift of complete period
- $180\degree$ one half period

### Example problem
- the power we use at home has a frequency of 60 Hz. The period of this sine wave can be determined through
$$\begin{align}
T &= \frac{1}{f} \\
&= \frac{1}{60} \\
&= 0.0167s \\
&= 16.7ms
\end{align}$$
- this means that the period of the power for our lights at home is 16.7ms, and our eyes are not sensitive enough to distinguish the rapid changes in this amplitude.

- #### express a period of 100 ms in microseconds

## Wavelength
- characteristic of a signal traveling through a transmission medium
- binds the period or the frequency of a simple sine wave to the propagation speed of the medium
- **wavelength depends on frequency and medium**
- distance that a simple signal can travel in one period
- wavelength $\lambda$ can be calculated given propagation speed and signal period or frequency
- $wavelength = propagationSpeed \times period = \frac{propagationSpeed}{frequency}$
- in a vacuum, light is propagated at $3\times10^{8}ms$, lower in air, even lower in cable
- wavelength measured in micrometers (microns) instead of meters
## Time and Frequency Domains
### Time-domain plot
- shows changes in signal amplitude with respect to time
- **amplitude vs time plot**
- phase not explicitly shown
### frequency domain plot
- show relationship between amplitude and frequency
- concerned only with peak value and frequency
- changes of amplitude during one period are not shown
## Applications of Simple Sine Waves
- power company sends single sine wave 60Hz to houses 
- send alarm to security center 
### in data comms
- only one single sine wave would not make sense
## Composite Signals
- early 1900s, Jean-Baptiste Fourier showed that any composite signal is a combination of simple sine waves with different frequencies, amplitudes, and phases (Fourier analysis)
- composite signal can be periodic or non-periodic
	- periodic composite:
		- decomposed into simple sine waves with discrete frequencies
	- nonperiodic composite 
		- decomposed into combination of an infinite number of simple sine waves with continuous frequencies
## Bandwidth
- range of frequencies contained in a composite signal
- normally a difference between two numbers (max and min)
	- bandwidth of composite signal is the difference between the highest and lowest frequencies contained in that signal
	- if a composite signal contains frequencies between 1000 and 5000, 
		- $bandwidth = 4000$
		- $bandwidth = freq_{max} - freq_{min}$
## Digital Signals
- 0 or 1, represented by a voltage spike
- can have more than two levels, with $2^{n}$ bits per level (am i sure? no.)
- in general, if a signal has $L$ levels, each level needs $log_{2}(L)$ bits (literally log form of $2^{n}$).
## Bit rate
- most digital signals are non-periodic,  
	- period and frequency are not appropriate characteristics
- bitrate is used for digital signals
	- number of bits sent in 1 second, expressed in bps
### Example
- What is the bit rate of HDTV?
	- HDTV uses digital signals to broadcast high quality video signals
	- normally a ratio of 16:9, assuming there are 1920 by 1080 pixels with a refresh rate of 30 Hz.
	- 24 bits represent 1 color pixel, we can calculate the bit rate then as
	- $1920 \times 1080 \times 30 \times 24 = 1,492,992,000 bps \approx 1.5Gbps$
	- tv stations reduce this rate to 20 to 40 Mbps via compression techniques such as mpeg

## Digital Signal as a Composite Analog Signal
- based on Fourier analysis, a digital signal is a composite analog signal
- the bandwidth is infinite
- in the time domain, it is comprised of connected vertical and horizontal line segments
	- vertical line in the time domain means frequency of infinity
	- horizontal lien in the time domain means a frequency of 0
	- going from zero to inf implies all frequencies in between are part of the domain


## The Telephone System
- originally created to provide voice comms
### Timeline
- need to communicate digital data lead to dial-up modem
- with internet came the need for high-speed downloading and uploading
	- the modem was just too slow
	- telephone companies added DSL (digital subscriber line), much faster than dial up modem
### Telephone Network
- uses circuit switching
	- connection-oriented
		- path established between source and destination before transmission
	- **packet switching** on the otherhand
		- connectionless
		- dynamic route decided for each packet while transmitting
- started in the late 1800s
- referred to as teh plain old telephone system (POTS)
	- analog signals transmitting voice
- 1980s carried data in addition to voice
- now digital as well as analog
## Major Components of Telephone Network System
### local loops
- twisted pair cable that connects the subscriber telephone to the nearest end office or local central office
- for voice, has bandwidth of 4000Hz (4kHz)
- first 3 digits of telephone number define the office, next 4 digits define local loop number
![[Pasted image 20231004111317.png|525]]
### trunks
- transmission media handles comms between offices
- handles hundreds or thousands of connections through multiplexing
- usually through optical fibers or sat links
### switching offices
- avoid having permanent physical link between any 2 subs
- connects several local loops or trunks for connection between diff subscribers
## Dial up modems
- traditional telephone lines can carry frequencies between 300 and 3300 Hz
	- bandiwdth 3000Hz (3kHz)
	 - range used for transmitting voice
	 - great deal of interference and distortion accepted w/o loss of intelligibility
- data sigs require higher degree of accuracy to ensure integrity
	- edges of this range are not used for data comms
- signal bandwidth for data transmission must be smaller than cable bandwidth
	- 2.4 kHz, 600-3000 Hz 
	- modern lines capable of higher bandwidth
- 