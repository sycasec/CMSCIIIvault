# Naive Bayes: Dealing with Continuous Data
```toc
```


## Probability of a probability density function
- remember that calculating the probability that $X$ is in the interval $(a,b)$ in a probability density function (p.d.f.) $\rho_X(x)$ require finding the area under the curve along the interval
	- the domain is $X$
	- the $x$ is just a random variable
	- so the $x$ in $\rho_X(x)$ is any value contained within $X$
- the interval is given by:
	- $P(a < X < b) = \int_a^b \rho_X(x)dx$
	- ![[Pasted image 20231115133715.png|325]]
## Dealing with continues attributes
Naive Bayes
### Step 1:
- assume that the continuous attribute $X_{i} \sim N(\mu_i,\sigma_i^2)$  (*normal distribution*)
	- another *naive* assumption of the algorithm
### Step 2:
- Approximate $P(X_{i}=x_{i} | Y=y_{j})\approx p_{X_{i}}(x=x_{i}|y_{j})$
- where 
	- ![[Pasted image 20231115134429.png|325]]
	- $\rho_{X_i}(x|y_j)=\frac{1}{\sigma_{i|y_j}\sqrt{2\pi}}e^{[-\frac{1}{2}(\frac{x-\mu_{i|y_j}}{\sigma_{i|y_j}})^2]}$
	- where $\mu_{i|y_j}$ and $\sigma_{i|y_j}$ are the mean and standard deviation of $X_i$ conditioned on $y_j$ respectively.
	- the mean and standard deviation of the values in $X_i$ are labelled by the class $y_j$.
### Step 3:
- perform the usual steps of naive bayes

## Why are we not taking the definite integral in Step 2??
shouldn’t we be taking the Area Under the Curve (AUC) since we are calculating probabilities?
- The probability of a single point is always zero for any continuous probability distribution, $P(X=x)=0$
- however, using the PDF, we can calculate the probability that $X$ lies in a narrow interval
	- $\left[x_{0}-\frac{\varepsilon}{2}, x_{0}+\frac{\varepsilon}{2} \right]$
	- around $x_0$ as:
	- $P(x_{0}- \varepsilon < X < x_{0}+\varepsilon) \approx \varepsilon \cdot \rho_{X}(x_0)$
		- ![[Pasted image 20231115143252.png|275]]
![[Pasted image 20231115142913.png|475]]
- Since $X_k$ is continuous, we cannot count its values as we do with the other features. Thus, the original equation becomes equal to:
	- ![[Pasted image 20231115143135.png|475]]
- ![[Pasted image 20231115143537.png|500]]
	- we assume that the marginal probability (denominator) = 1
- ![[Pasted image 20231115144010.png|500]]

## Example 
Tumor Detection with mixed data

| Sample | Gene A | Gene B | Gene C | Gene D | Class   |
| ------ | ------ | ------ | ------ | ------ | ------- |
| 1      | 1      | 35     | 1      | 0      | normal  |
| 2      | 1      | 30     | 1      | 1      | normal  |
| 3      | 0      | 32     | 1      | 0      | tumor   |
| 4      | -1     | 20     | 1      | 0      | tumor   |
| 5      | -1     | 15     | 0      | 0      | tumor   |
| 6      | -1     | 13     | 0      | 1      | normal  |
| 7      | 0      | 11     | 0      | 1      | tumor   |
| 8      | 1      | 22     | 1      | 0      | normal  |
| 9      | 1      | 14     | 0      | 0      | tumor   |
| 10     | -1     | 24     | 0      | 0      | tumor   |
| 11     | 1      | 23     | 0      | 1      | tumor   |
| 12     | 0      | 25     | 1      | 1      | tumor   |
| 13     | 0      | 33     | 0      | 0      | tumor   |
| 14     | -1     | 21     | 1      | 1      | normal  |
| 15     | 1      | 12     | 1      | 1      | unknown | 

- unseen data is given by $\vec{x}^{15}= (1,12,1,1)$
- we want to predict its class given the training dataset in the table at the right

### Step 1: Normality Assumption
- assume that Gene B is normally distributed
### Step 2: approximate the likelihood of the continuous attribute given the class
- we approximate the likelihood as follows:
- normal:
	-  $P(B=12 | normal) = N(\mu_{B|normal}, \sigma^2_{B|normal})$
	- we need to compute the mean and the standard deviation for class $normal$ (parameters of the Gaussian PDF)
		- $y=normal$
			- $\mu_{B|normal} = \frac{35+30+13+22+21}{5} = 24.2$ 
			- $\sigma_{B|normal} \approx 8.526$
			- $\rho_{B}(x=12|normal) = \frac{1}{\sigma_{B|normal}\sqrt{2\pi}}e^{\left[-\frac{1}{2} \left(\frac{x-\mu_{B|normal}}{\sigma_{B|normal}} \right)^2 \right]}$
			- $\rho_{B}(x=12|normal) = \frac{1}{8.5\sqrt{2\pi}}e^{\left[-\frac{1}{2} \left(\frac{12-24.2}{8.5} \right)^2 \right]}$
			- = 0.01676
		-  $y=tumor$
			- $\mu_{B|tumor} = \frac{32+20+15+11+14+24+23+25+33}{9} = 21.9$ 
			- $\sigma_{B|tumor} \approx 7.7$ 
			- $\rho_{B}(x=12|tumor) = \frac{1}{\sigma_{B|tumor}\sqrt{2\pi}}e^{\left[-\frac{1}{2} \left(\frac{x-\mu_{B|tumor}}{\sigma_{B|tumor}} \right)^2 \right]}$
			- $\rho_{B}(x=12|tumor) = \frac{1}{7.7\sqrt{2\pi}}e^{\left[-\frac{1}{2} \left(\frac{12-21.9}{7.7} \right)^2 \right]}$
			- 0.0227
### Step 3: Perform the regular naive Bayes algorithm
- calculate the relative likelihood as previous calculations
	- $P(normal|\vec{x}^{15}) = \frac{(\frac{3}{5})(0.01676)(\frac{4}{5})(\frac{3}{5})(\frac{5}{14})}{P(\vec{x}^{15})} = \frac{0.00172}{P(\vec{x}^{15})} \propto 0.00172$
	- $P(tumor|\vec{x}^{15}) = \frac{(\frac{2}{9})(0.0227)(\frac{1}{3})(\frac{1}{3})(\frac{9}{14})}{P(\vec{x}^{15})} = \frac{0.00036}{P(\vec{x}^{15})} \propto 0.00036$
- the marginal probability (denominator) is just the sum of these both
- we can now calculate the posterior likelihood, similar with previous naive bayes
	- $P(normal|\vec{x}^{15}) = \frac{0.00172}{0.00172+0.00036} \approx 0.827$
	- $P(tumor|\vec{x}^{15}) = \frac{0.00036}{0.00172+0.00036} \approx 0.173$


## Why do we assume normality for the continuous attribute?
### Applicability
- the assumption of normality is often a reasonable approximation for many real-world data distributions
### Simplicity
- the normal distribution is one of the most well studied and understood distribution, making it a natural choice
### Computational Efficiency
- the pdf of the normal distribution is relatively simple to compute, which makes it efficient to use in Naive Bayes calculations
### Robustness
- the naive bayes classifier is relatively robust to violations of the assumption of normality, making it a practical choice
## Can we use other distributions?
- the normality assumption (assuming the continuous data follows a normal distribution) is not strictly necessary for the Naive Bayes model to work
- we can use other distributions especially if they better fit the data
### Alternatives
- Kernel Density Estimation
	- plot the distribution of the data
	- fit the kernel density of that distribution
	- minimize the bin size of the histogram, so that it becomes continuous
- Discretization
	- turn the continuous attribute into discrete
### implication of the Central Limit Theorem
- if we have a normally distributed set of data points, if we randomly sample subsets of that data we get a normal distro
	- provided the elements of the subsets are drawn randomly 



## Quiz
| Sample No. | Chol | FBS | Restecg | Exang | Oldpeak | Class |
| ---------- | ---- | --- | ------- | ----- | ------- | ----- |
| 1          | 184  | 0   | 0       | 1     | 2.1     | 0     |
| 2          | 243  | 0   | 0       | 1     | 0       | 1     |
| 3          | 222  | 0   | 1       | 1     | 1.2     | 1     |
| 4          | 309  | 0   | 0       | 1     | 0       | 0     |
| 5          | 198  | 0   | 1       | 1     | 1.6     | 0     |
| 6          | 308  | 0   | 0       | 0     | 0       | 1     |
| 7          | 234  | 0   | 0       | 0     | 0       | 1     |
| 8          | 197  | 0   | 0       | 0     | 0       | 0     |
| 9          | 266  | 0   | 0       | 1     | 2.2     | 0     |
| 10         | 195  | 0   | 1       | 0     | 0       | 1     |
| 11         | 223  | 0   | 1       | 0     | 0       | 1     |
| 12         | 309  | 0   | 1       | 0     | 0       | 1     |
| 13         | 233  | 1   | 0       | 0     | 2.3     | 1     |
| 14         | 289  | 1   | 0       | 0     | 1       | 0     |
| 15         | 235  | 0   | 1       | 0     | 0       | 1     |
x_unknown = np.array([193, 1, 1, 0, 3.4])

| Chol | FBS | Rest | Ex  | Old |
| ---- | --- | ---- | --- | --- |
| 193  | 1   | 1    | 0   | 3.4 |
| 241  | 0   | 1    | 1   | 0.2    |


**Class 0**
chol = 0.005
oldpeak = 0.030
FBS = 0.167
Rest = 0.167
Exang = 0.333
P(Class = 0) = 0.4
0.000 000 557 222 22

Class 1
chol = 0.004
oldpeak = 0.001
fbs = 0.111
rest = 0.556
exang = 0.778
P(Class = 1) = 0.6
0.000 000 115 236 115 2

total = 0.000 000 672 458 335 2

class 1
0.171 365 435 1
class 0 
0.828 634 564 9