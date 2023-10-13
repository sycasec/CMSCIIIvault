
[[MachineLearning]]

# Linear Regression Problem 
```toc
```

- finding the best fit line in a scatterplot
- showing the correlation /  relationship of 2 features (X, Y)
	- assuming they are linear

## Ordinary Least Squares
- estimate the parameters of the best fit line
- in the context of **OLS**, the *best model* is the model that **minimizes the sum of the squared residuals between observations and predictions**

### How do we select the best model?
- OLS Criterion
- minimizes sum of the squared residuals
#### Residual
- distance from single point to line model
- $\epsilon_{i}= Y_{i}- \hat{Y}_i$
	- $= Y_{i}- (\beta_{0}+ \beta_{i}X_i)$

#### Selecting the best model
- minimize $E(\beta_{0}, \beta_{1}) = \sum_{i=1}^{n} (\epsilon_{i})^2$
	-  $= \sum_{i=1}^{n} (Y_i-(\beta_{0} + \beta_{i}X_i))^2$
		- also known as the cost function
	- $\nabla E(\beta_{0}, \beta_{1})=\left<\frac{\partial E}{\partial \beta_{0}}, \frac{\partial E}{\partial \beta_{1}}\right> = <0,0>$
	- computing for $\beta_0$
		- after derivation in terms of $\beta_0$
			- $0 = \frac{\partial}{\partial \beta_{0}} \sum\limits_{i=1}^{n} (Y_{i} - \beta_{0} - \beta_{1}X_{i})^2$
		- $\beta_{0} \approx \hat{\beta_{0}} = \bar{y}-\hat{\beta_{1}}\bar{x}$
	- computing for $\beta_1$
		- $0 = \frac{\partial}{\partial \beta_{1}} \sum\limits_{i=1}^{n} (Y_{i} - \beta_{0} - \beta_{1}X_{i})^2$
		- $\beta_{1} = \frac{\sum\limits_{i=1}^{n}(X_i-\bar{x})(Y_{i}-\hat{y})}{\sum\limits_{i=1}^{n}(X_{i}-\hat{x})^2}$
### What is the “best” model? 


## MLE
- $Y_{i} = \beta_{0}+\beta_{1}X_{i}+\epsilon_{i}$

### random variable $\epsilon_i$
- $\epsilon_{i} \approx N(0, \sigma^2)$
- minimize $\epsilon_{i}$ 
	- assume that it is 0

### Determine the distribution of $Y_i$

- $E[Y_{i}] = E[\beta_{0}+\beta_{1}X_{i}+\epsilon_{i}]$
	- $= E[\beta_{0]}+ E[\beta_{1}X_{i}] + E[\epsilon_{i}]$
	- **$\beta_{0}+\beta_{1}X_{i}$ is deterministic**
	- $= \beta_{0}+\beta_{1}X_{i}$
	- 