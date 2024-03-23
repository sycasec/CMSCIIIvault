# Naive Bayes
```toc
```

## Independence
Let A and B be events, we say that A and B are independent (written as $A \coprod B$)
if and only if:
$$\begin{aligned}
P (A \cap B) = P(A) \cdot P(B) 
\end{aligned}$$
**Rolling a fair, six-sided die**
- we want to know if “getting numbers less than equal to 4 is independent of getting odd numbers”

### Solution
- Event A = getting numbers less than or equal to 4 = $A = \{1,2,3,4\}$
- Event B = getting odd numbers = $B = \{1,3,5\}$
- Sample space $S = \{1,2,3,4,5,6\}$
- $A \cap B = \{1,3\}$
- $|A|$ = cardinality of A = amount of elements in A
#### Get probabilities
- $P(A) = \frac{|A|}{|S|} = \frac{2}{3}$
- $P(B) = \frac{|B|}{|S|} = \frac{1}{2}$
- $P(A \cap B) = \frac{|A \cap B|}{|S|} = \frac{2}{6} = \frac{1}{3}$
- check if $P(A \cap B) = P(A) \cdot P(B)$
	- they **are** equal, therefore A and B are independent events

## Conditional Independence
- conditioning, even if you have dependent events, we can condition them with another variable
- if we add a third event $C$, we use the events that intersect with $C$
- ![[Pasted image 20231114172630.png|625]]
### formal definition
- Let $A, B,$ and $C$ be events. Then $A$ and $B$ are said to be conditionally independent given $C$
- written as $(A \coprod B | C )$ if and only if:
	- $P(A\cap B|C) = P(A|C) \cdot P(B|C)$
	- and $P(C) > 0$
 - ![[Pasted image 20231114173112.png|550]]
 - $P(A|C) = \frac{|A \cap B' \cap C|+|A \cap B \cap C|}{|C|}$
	 - $= \frac{4}{20} = \frac {1}{4}$
 - $P(B|C) = \frac{1}{5}$
 - $P(A \cap B | C) = \frac{|A \cap B \cap C|}{|C|}$
	 - $= \frac{1}{20}$
 - therefore, conditionally independent

## The Naive Bayes Classifier
### Bayes Theorem
- mathematical formulation for determining conditional probabilities
- conditional probability is the likelihood of an outcome occuring, given a set of previous outcomes that occured in similar circumstances 
- provides a way to update our predictions or theories given new or additional evidence 
	- we can update our model given new data 
- let A and B be events. The bayes’ theorem is stated as follows:
$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B|A)\cdot P(A)}{P(B)}$$
- this is the simplest formulation of the theorem 
- if the sample space $\Omega$ can be divided into finitely many mutually exclusive events $A_{1}, A_{2}, ..., A_{n}$ and if $B$ is an event with $P(B) > 0$, which is  a subset of the union of all $A_i$, then for each  $A_i$ the generalized Bayes’ formula is 
$$P(A_{i}|B) = \frac{P(B|A_{i}) \cdot P(A_{i})}{\sum^{n}_{j=1}P(B|A_{j})\cdot P(A_{j})}$$
which can be restated as 
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B|A) \cdot P(A) + P(B|A') \cdot P(A')}$$

- ![[Pasted image 20231114192156.png|432]]

### Semantics of Bayes’ Theorem
- a more intuitive way to understand the meaning of Bayes’ theorem is by associating the terms: (i) hypothesis and (ii) data
- the hypothesis is our model. In classification, this might be the predicted class of the data. In this case, we want to test if a certain input belongs to a certain class
- The data is the evidence that we use to test the hypothesis. **Bayes’ theorem allows us to update our belief about the hypothesis based on the new data as follows:**
	- we can test the effectiveness of our model by using the data
$$P(H|D) = \frac{P(D|H) P(H)}{P(D)}$$
- $P(H|D)$ - represents the updated reliability of our model (H) given data (D)
- $P(H)$ - is just our model
- $P(D|H)$ - *probably* just the output of H → the best H is the one that gives a more correct D
	- probability of data D occurring if our hypothesis is correct, not sure what that means
- $P(D)$ - marginal probability of D irrespective of the specified hypothesis
	- we marginalize across all the hypothesis (??) to compute this value

### Example
Suppose we want to predict whether or not it will rain given that there are dark clouds. Let H be the event “raining” and D be the event “presence of dark clouds”.
We can express this using Bayes’ theorem as follows:
$$P(Rain | Dark clouds) = \frac{P(Dark\ clouds | rain) \cdot P(rain)}{P(dark\ clouds)}$$

- $P(Rain | Dark\ clouds)$ probability of rain given that we observe dark clouds
- $P(Rain)$ is the prior probability of rain, can be obtained from statistical records
- $P(Dark\ clouds|Rain)$ likelihood of having dark clouds when it rains, because there can be rain without dark clouds, there can also be dark clouds without rain. they have to exist together
- $P(Dark\ clouds)$ likelihood of dark clouds, raining or not

### How to use Bayes’ theorem for classification?
- Suppose we have a dataset containing n instances, $\vec{x_{i}}$ where $i=1,...,n$
- contains $p$ features so that $\vec{x_{i}} = (x_{i1},...,x_{ip})$ 
- each instance is assumed to belong to one and only one class $y \in {y_1,...,y_c}$ 
#### I like your funny words magic man
- its just a dataset with $p$ features (columns) and $n$ rows
- each element can only belong to one class (cat or dog => cat image slice or dog image slice)
	- (certain (x,y) of an image that is either a dog particle or a cat particle, cannot be both!)
- bayesian learning classifies inputs into the class with the maximum score:
	- $\hat{y} = arg max P (y = y'|\vec{x_z})$
	- we assign the class with the maximum probability to the object
-![[Pasted image 20231114200129.png|575]]
- ![[Pasted image 20231114210106.png|575]] 
- by assuming conditional independence however, we can avoid this NP hard problem, reducing data vector $\vec{x_z}$ to:
	- ![[Pasted image 20231114232507.png|525]]

### Naive Bayes Classifier
finally, we can express it in a more compact form as follows:
$$P(y=y_{j}|x_{z1},...,x_{zp}) = \frac{\prod^{p}_{i=1}P(x_{zi}|y_{j}) \cdot P(y_{j})}{\prod^{c}_{k=1}(\prod^{p}_{i=1}P(x_{zi}|y_{k})\cdot P(y_{k}))}$$
- this *naively* assumes conditional independence given the class
- in many cases, conditional independence may not exist. However, naive Byes doesn’t care, which is why its a naive version of Bayes’ theorem
- in some cases, we do not care about posterior probabilities, we only want to rank the classes
	- we do not need to compute the marginal probability of the data.
		- (the argmax equation, is this more likely to be a cat or a dog?)
	- this simplifies the computation to the form:
	- $P(y=y_{j}|x_{z1},...,x_{zp}) \propto \prod\limits^{p}_{i=1}P(x_{zi}|y_{j})\cdot P(y_{j})$
		- regarding the previous equation, we assume the denominator is 1 because we do not care about its value
		- the left side is proportional to the right side. 
	- it has performed well in many applications.
	- in general, when the inherent relationships between the variables are important, naive Bayes may not be a good model.

#### Sample Problem - Tumor Detection
| Sample | Gene A | Gene B | Gene C | Gene D | Class   |
| ------ | ------ | ------ | ------ | ------ | ------- |
| 1      | 1      | 1      | 1      | 0      | normal  |
| 2      | 1      | 1      | 1      | 1      | normal  |
| 3      | 0      | 1      | 1      | 0      | tumor   |
| 4      | -1     | 0      | 1      | 0      | tumor   |
| 5      | -1     | -1     | 0      | 0      | tumor   |
| 6      | -1     | -1     | 0      | 1      | normal  |
| 7      | 0      | -1     | 0      | 1      | tumor   |
| 8      | 1      | 0      | 1      | 0      | normal  |
| 9      | 1      | -1     | 0      | 0      | tumor   |
| 10     | -1     | 0      | 0      | 0      | tumor   |
| 11     | 1      | 0      | 0      | 1      | tumor   |
| 12     | 0      | 0      | 1      | 1      | tumor   |
| 13     | 0      | 1      | 0      | 0      | tumor   |
| 14     | -1     | 0      | 1      | 1      | normal  |
| 15     | 1      | -1     | 1      | 1      | unknown |

we want to predict the unseen data given by $\vec{x^{15}} = (1,-1,1,1)$

##### Step 1: Build the Conditional Probability Table 
- count all the occurrences of each value in each class 
- ![[Pasted image 20231114234239.png|500]]

|       | Gene A | Gene A | Gene B | Gene B |
| ----- | ------ | ------ | ------ | ------ |
|       | Normal | Tumor  | Normal | Tumor  |
| +1    | 3      | 2      | 2      | 2      |
| 0     | 0      | 4      | 2      | 4      |
| -1    | 2      | 3      | 1      | 3      |
| total | 5      | 9      | 5      | 9      |
|       | Gene C | Gene C | Gene D | Gene D | 
|       | Normal | Tumor  | Normal | Tumor  |
| +1    | 4      | 3      | 3      | 3      |
| 0     | 1      | 6      | 2      | 6      |
| -1    | 0      | 0      | 0      | 0      |
| total | 5      | 9      | 5      | 9      |
##### Step 2: Compute the prior probabilities in each class
**for class “Tumor”**
- $P(tumor|\vec{x}^{15}) = P(A = 1|tumor) \cdot P(B = -1|tumor) \cdot P(C = 1 |tumor) \cdot P(D = 1 | tumor) \cdot P(tumor)$
- $P(tumor|\vec{x}^{15}) = (\frac{2}{9})(\frac{1}{3})(\frac{1}{3})(\frac{1}{3})\left(\frac{9}{14}\right) \propto 0.00529$ 

**for class “Normal”**
- $P(normal|\vec{x}^{15}) = P(A = 1|normal) \cdot P(B = -1|normal) \cdot P(C = 1 |normal) \cdot P(D = 1 | normal) \cdot P(normal)$
- $P(normal|\vec{x}^{15}) = (\frac{3}{5})(\frac{1}{5})(\frac{4}{5})(\frac{3}{5})\left(\frac{5}{14}\right) \propto 0.02057$ 

if only class is asked, we can already determine that the data vector $\vec{x}^{15}$ is of class normal due to class normal being of higher probability than class tumor given the training dataset



##### Posterior Probability Computation
notice that the marginal probability of the data is just 
$P(\vec{x}^{15})= P(tumor|\vec{x}^{15}) = P(A = 1|tumor) \cdot P(tumor) + P(normal|\vec{x}^{15}) \cdot P(normal)$
it follows that $P(\vec{x}^{15}) = 0.00529 + 0.02057 = 0.02586$
thus, the posterior probabilities are:

$P(tumor|\vec{x}^{15)}= \frac{0.00529}{0.02586} = 0.2046$
$P(normal|\vec{x}^{15})=\frac{0.02057}{0.02586}=0.7954$

since P(normal) > P(tumor), $\vec{x}^{15}$ belongs to class normal

#### Laplace Smoothing
- when the number of samples is small
- if Gene A is underexpressed (-1) in instances #9 and #11 in teh data
	- $P(A = 1 | tumor) = 0$, implying that it is impossible to observe Gene A in a sample class $tumor$
	- is it wise to make this assumption? no it is better to allow for a small, non-zero probability
- adds a small pseudo count to each of the feature of probabilities
- helps ensure that all features have non-zero probability, even if they are not observed in the training data
- common value to add is 1, however this has to be made relative to the **size** dataset 
	- instead of adding one, other options can also be considered

##### using Laplace smoothing **(by adding 1)**, the previous values can be adjusted
- ![[Pasted image 20231115131716.png|275]]
- ![[Pasted image 20231115131806.png|275]]
- 3 is added to the denominator since 3 values are being added to the feature
##### using Laplace smoothing by adding a **small positive constant**
- ![[Pasted image 20231115132014.png|300]]


