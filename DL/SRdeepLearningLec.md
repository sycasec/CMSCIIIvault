---
date_created: 2024-02-15
date_modified: 2024-02-15
type: lecture notes
topic: Seb Rasch Deep Learning
entry number: "0"
---

# Sebastian Raschka Deep Learning
**Current Trends**
- Graph neural networks
	- graph structured data
	- can be used to model molecules
	- bla

## Perceptron - single layer networks
- rosenblatt’s perceptron (*1957*)
- ![[Pasted image 20240215013327.png|500]]
- based on neuron
- $x_{1}...x_{m}$  := feature vector
- each multiplied with a weight → weighted sum
```python
class Perceptron():
	def __init__(self, num_features):
		self.num_features = num_features
		self.weights = np.zeroes((num_features, 1), dtype=np.float)
		sefl.bias = np.zeroes(1, dtype=np.float)

	def forward(self, x);
		linear = np.dot(x, self.weights) + self.bias
		preds = np.where(linear > 0., 1, 0)
		return preds

	def backward(self, x, y):
		preds = self.forward(x)
		errors = y - preds
		return errors

	def train(self, x, y, epochs):
		for e in range epochs:
			for i in range(y.shape[0]):
				errors = self.backward(x[i].reshape(1, self.num_features))
				self.weights += (errors * x[i]).reshape(self.num_features)
				self.bias += errors

	def evaluate(self, x, y):
		preds = self.forward(x).reshape(-1)
		accuracy = np.sum(preds == y) / y.shape(0)
		return accuracy
```

## Fundamental Linear Algebra for Deep Learning
### Tensors
- a generalization of *Vectors*, *Scalar*, and *Matrix*
- **Scalar**
	- rank 0 tensor
- **Vector**
	- rank 1 tensor
- **Matrix**
	- rank 2 tensor

- **X** as a special convention that refers to the design matrix
	- contains training examples and features 
	- convention is $X ^ {(n \times m)}$ 
		- where $n$ is the number of training examples (entries, rows, etc)
		- where $m$ is the number of features (labels, columns, etc)
### Broadcasting
#### $w^{\top} x + b = z$
- $z$ is the net input
- x is the entries
- w is the weights duh
#### Computing output from multiple training examples at once
 - perceptron is typically considered “*online*”
	 - updates the weights after each training example/entry/row

## Gradient Descent
### Training Neural Nets: Online, Batch, and Minibatch modes
#### Perceptron Recap
- ![[Pasted image 20240222100829.png|450]]
- ![[Pasted image 20240222100904.png|450]]
#### General Learning Principle
- mini batch mode is the most common in ML
##### On-line mode
- $w \rightarrow\ weight$
- $b \rightarrow\ bias$
1. Initialize $w := 0 \in \mathbb{R}^{m,}b:= 0$
2. For every training epoch
	1. For every data point $\left<x^{[i]},y^{[i]}\right>\in D$
		1. Compute output (prediction)
		2. Calculate error
		3. Update weight and bias

##### Batch-mode
Basically hypertrain a model by updating weights and biases every epoch, it is expected to do multiple epochs
- you do one update every epoch (one go through the entire dataset)

1. Initialize $w := 0 \in \mathbb{R}^{m,}b:= 0$
2. For every training epoch
	1. Initialize $\Delta w:=0, \Delta b:=0$
	2. For every datapoint:
		1. compute output 
		2. calculate error
		3. update delta weight and bias
	3. update weight and bias:
		- $w := w + \Delta w,b:=+ \Delta b$
		
##### mini-batch mode
- mix of batch and online
- k is a hyperparameter
	- in literature, usually 16, 32, 64
- most common used in DL → why?
	- faster due to batching, smaller matrix multiplications
	- makes updates less noisy, more robust


1. Initialize $w := 0 \in \mathbb{R}^{m,}b:= 0$
2. For every training epoch
	1. For every minibatch of size $k$
		2. Initialize $\Delta w:=0, \Delta b:=0$
		3. For every datapoint:
			1. compute output 
			2. calculate error
			3. update delta weight and bias
		4. update weight and bias:
			- $w := w + \Delta w,b:=+ \Delta b$

### Linear regression as a single-layer neural network
![[Pasted image 20240222103651.png|550]]
#### Stochastic Gradient Descent Online iterative
- $\eta$ → learning rate

1. init w, b
2. for each training epoch
	1. for each data point
		-  $\hat{y}^{[i]}=\sigma(x^{[i]\top}w + b)$
		- $\nabla_{w}\mathcal{L}=(y^{[i]}=\hat{y}^{[i]})x^{[i]}$
		- $\nabla_{b}\mathcal{L}=(y^{[i]}=\hat{y}^{[i]})$
		- $w += \eta \times (-\nabla_{w}\mathcal{L})$
		- $b += \eta \times (-\nabla_{b}\mathcal{L})$

#### Vectorized and For-loop
![[Pasted image 20240222110455.png|500]]


### Calculus refresher
- Derivative of a function = “rate of change / slope”
- ![[Pasted image 20240222110711.png|550]]
## ADALINE
- widrow and hoff’s adaline 1960
- converging even if the data is not linearly separable
- ![[Pasted image 20240215022817.png]]
- in comparison with perceptron, error is computed before threshold function
	- gradients are computed before the threshold function
	- threshold function still not differentiable
- very similar to linear regression 
	- the only difference is that we apply threshold function to convert outputs from continuous targets for predictions
	- derivative and training procedure identical to ADALINE

### Code Example
#### Linear Regression PyTorch
```python
import torch

class LinearRegression():
	def __init__(self, num_features):
		self.num_Features = num_features
		self.w = torch.zeros(num_features, 1, dtype=torch.float)
		self.b = torch.zeroes(1, dtype=torch.float)

	def forward(self, x):
		netinputs = torch.add(torch.mm(x, self.w), self.b)
		activations = netinputs
		return activations.view(-1)

	def backward(self, x, yhat, y):
		grad_loss_yhat = 2*(y - yhat)
		grad_yhat_w = x
		grad_yhat_bias = 1.
		# Chain rule
		grad_loss_w = torch.mm(grad_yhat_w.t(),
								   grad_loss_yhat.view(-1,1)
		) / y.size(0)
		grad_loss_b = torch.sum(grad_yhat_b * grad_loss_yhat) / y.size 0
		return (-1)*grad_loss_w, (-1)*grad_loss_bias

	def loss(yhat, y): # Mean Squared Error
		return torch.mean((yhat - y) ** 2)

#Batch Training
	def train(model, x, y, num_epochs, learning_rate=0.01):
		cost = []
		for e in range(num_epochs):

			# compute outputs
			yhat = model.forward(x)

			# compute gradients
			neg_grad_w, neg_grad_b = model.backward(x, yhat, y)


			# update weights
			model.w += learning_rate * neg_grad_w
			model.b += learning_rate * neg_grad_b

			# log
			yhat = model.forward(x) # consumes computation time
			curr_loss = loss(yhat, y)
			print("Epoch: %03d" % (e+1), end="")
			print(" | MSE: %.5f" % curr_loss)
			cost.append(curr_loss)

		return cost
```

