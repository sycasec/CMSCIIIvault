---
date_created: 2024-02-05
---

# Deep Learning Lecture 2
## Basic Principles of ANN Design
- formulated by MuCulloch & Pitts 1943
	- activity of neuron is all or nothing: binary element
	- fixed synapses (weights) larger than 1 must be excited within a given interval of neural addition for a neuron to be excited
		- neuron will not activate if previous neuron does not
		- neuron activation must come from origin
		- sequential
	- synaptic delay is the only significant delay within the neural system
		- define computational steps → all other delays are not considered
	- any inhibitory synapse absolutely prevents the excitation of the neuron
		- one layer must be activated before another layer
	- structure does not change over time
## Hebbian Learning
- proposed by Donald Hebb in 1949
- if axon of cell A is near enough to excite cell B
	- and if cell A repeatedly and persistently takes part in the activation of cell B
	- some growth process takes place in one or both cells such that the efficiency of cell A is increased
	- **TL;DR** neurons that fire together wire together
- foundation for early neural networks
- more sophisticated algos like backprop and supervised approaches became dominant

## Perceptron
- one of the earliest neural computation model
- Frank Rosenblatt’s paper in 1957
- fundamental structure of neuron
	- connects several weighted input connections at the input-side to the output-side
- the perceptron uses the signum function as the activation function
	- only 3 classifications
	- signum function is basically a piece-wise function that groups results into `[ -1, 0, 1 ]`

### Formal Definition
-  binary classifier iteratively learns a function
- $f:  x \rightarrow y$ where $x \in \R ^{p}$ and $y \in {-1,1}$
- $\hat{f}(x) = \sigma(w \cdot x + b)$
- How do we learn these weights?
	- initialize weights to zero or random values
	- for each example $(x_{b} y_{i}) \in D$ in our training data, peform the following:
		- calculate prediction $\hat{y} = \hat{f}(x) = \sigma(w \cdot x + b)$
		- update the weights using the error signals as follows
			- $w_{j}^{[i+1]}=w_{j}^{[i]}+\Delta w_{j}^{[i]}$
		- error computation
			- where $\Delta w_{j}^{[i]} = \eta(y^{[i]}-\hat{y}^{[i]})x_{j}^{[i]}$
			- to update bias, in the above error computation change $x_{j}^{[i]}$ to 1
	- 