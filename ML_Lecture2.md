[[MachineLearning]]

# Maximum Likelihood Estimation

### Step 1 
-  Determine the distribution of each random Variable $X_{i} \approx f(X_i|\theta)$
### Step 2
- Build the likelihood (or log-likelihood if applicable) function given the dataset $X = [x_{1}, x_{2,} ..., x_n]$

### $$L(\theta|X) = P(X_{1} = x_{1},..., X_{n}= x_{n}| \theta) = \prod_{i=1}^{n} f(x_i|\theta) $$
### Step 3
- Compute the values of the parameters $\theta$ that give the maximum likelihood by solving the optimization problem

$$\hat{\theta} = arg\ max \ L(\theta|X)$$


## Sample : Bernoulli

### Step 1 
$$X \approx Bern(p)$$

### Step 2 - build the likelihood function
- find the joint distribution given dataset

$$L(p|X) = P(X_1=x_{1},...,X_n=x_n|p)$$
$$= \prod_{i=1}^{n} f(X_i|p)$$
- The bernoulli distribution is given by its pmf :
$$P(x)= p^{x}(1-p)^{1-x}$$
- Substitute the PMF given above to the $f$ in the product **loop**
$$\prod_{i=1}^{n}p^{X_i}(1-p)^{1-X_i}$$
