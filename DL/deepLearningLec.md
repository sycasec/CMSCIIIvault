# Deep Learning Lecture
```toc
```

## Brain as inspiration for computing
- inspired of information processing
- ANN is named after biological neural networks
- artificial neurons
	- communicate via synapse
	- allows us to define ANN precisely with mathematical notations
## Phases of ANN
- Singel layer
- Early Multi layer networks
- deep neural networks

### Single Layer
- single processing neuron
- perceptron consists of a single neuron with the following activation function
$$
\begin{equation}
f(a) =
\left\{
	\begin{array}{lr}
		0, & \text{if } a \leq 0\\
		1, & \text{if } a > 0
	\end{array}
\right\} 
\end{equation}
$$
- typical perceptron had multiple layers of processing, only one of those layers was learning from data
	- single layer because only one layer was learning from data
### Backpropagation
- solution to multi layer networks 
	- differential calculus
	- gradient-based optimization
### CNN
- extracts useful features
- depth plays an integral role in performance