[[MachineLearning]]
```toc
```

# Gauss Markov Theorem
- the OLS estimator has the lowest sampling variance 
- the distribution of $\epsilon_i$ does not matter, it only matters that $E[x] = \bar{x}=0$


# Supervised Learning: Classification

- previous lectures revolve around estimate parameters of probability distributions
	- conditional expectations of continuous variables
- we will now be predicting a categorical variable class given a set of independent variables
	- class for dependent variable (The thing we are predicting)
	- feature for the independent variables we train and supply the model
- binary classification

## Linear Regression
- calculate best fit line given two features
	- we can calculate $R^2$ and determine if the two features are correlated
		- large values imply a large effect
	- we can calculate p value to determine if $R^2$ is significant
	- we can also use the line to predict one feature given the other
## Multiple Regression
- Linear regression but with more dimensions / features
## Logistic Regression
$$log\left(\frac{p(\vec{x})}{1-p(\vec{x})}\right)=\hat{p}_{0}+\vec{x}\ \cdot \ \vec{\hat{p}}$$
- predicts whether something is true or false
- fits an S shaped function
- used for classification
- continuous / discrete data can be used
### Coefficients
- 

## Gradient Descent
- 