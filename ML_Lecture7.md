# K Nearest Neighbors
```toc
```

## KNN Algorithm
- compute distance unknown object to closest distance of certain radius
	- sort distance
- class of unknown object is based on majority class of k nearest neighbors

### Formal Definition
1. Decide the number of nearest neighbors $k$
	- there are some techniques to determine $k$
2. Compute the distance of an unlabeled data point $z = (\vec{x}', y')$ given all training examples $(\vec{x}^{(i)}, y^{(i)})$ in $D$ 
3. sort all distances from $z$
4. Select the first $k$ points of the sorted distances
5. Assign the majority class of the $k$ nearest neighbors to $y'$

### Description
- KNN is a nonparametric classification algorithm
- has no distributional assumption
- determines membership of unlabeled sample based on majority of the k labeled samples’ class
- in a nutshell, KNN assigns similar labels to unknown objects with similar feature values
- KNN does not actually build a model, parameters are not learned 
	- black box
### Pseudo-code for standard KNN
```py
# let k be the number of nearest neighbors, and D be the set of training examples
distances = {}

for each test instance z = (vec_x_prime, y_prime) :
	for each training example (x_i, y_i) in D:
		Compute distance(vec_x_prime, x_i), the distance between z and every training example
		distances['node'] = [distance, x, y, class]
	end

	# sort distances and get k nearest distances
	k_nearest = distances.items().sort()
	k_nearest = k_nearest[:k]

	# assign y to majority class
	idk how
end
```



## Proximity Measures
- In Nearest-neighbors classification, we need ways to asses how alike or unalike objects are in comparison from one another
- these similarities or dissimilarities are referred to as proximity measures

### Similarity Measure
- returns 0 if objects are different
- positive value if objects are similar
### Dissimilarity Measure
- opposite to similarity
- returns 0 if objects are the same
	- can be represented by the piece-wise function:
$$
\begin{equation}
d(x,y) =
\left\{
	\begin{array}{lr}
		0, & \text{if } x = y\\
		1, & \text{if } x\neq y
	\end{array}
\right\} 
\end{equation}
$$
- straightforward way of representing dissimilarity of two objects
	- many methods, there is active research on methods to dissimilarity measures that would yield better performance for certain algorithms
- returns high positive value if objects are dissimilar
#### Nominal Attribute Dissimilarity
- nominal attributes are categorical attributes that do not have any meaningful order
- we assign numeric values to these attributes for encoding purposes
- 
### Example - Nominal
- Suppose our data vector is given by the following type:
	- $<Vector> T = [ < Season >, < Temperature >, < Indicator >]$
	- given samples $x = (Winter,\ Cold,\ Snow), y=(Wet,\ Cold,\ Rain)$
	- compute dissimilarities as follows:
	- `for each item in x: return 1 if x != y else 0` 
### Example - Ordinal
- categorical with meaningful order or ranking
- magnitude separating each ranking is not known
- when assigning encoding (artificial numerical values), the value positivity does not matter, only that the ranking is preserved
- Suppose we have 2 ordinal features 
	- `educational_level = { Elementary, High School, Undergrad, Grad}`
	- `income = {low, mid, high}`
 - Calculate dissimilarity between $x = (Highschool,\ middle)$ and $y=(Graduate,\ High)$

1. Assign artificial numeric values to each ordinal attribute to encode the order
	- `educ_level = {"elem": 1, "hs": 2, "ug": 3, "g": 4}`
	- `income = {"low": 1, "mid": 2, "high": 3}`
2. Convert vector using encoding
	- x → x’ = $(2,2)$
	- y → y’ = $(4,3)$ 
3. calculate dissimilarity
	- $d(x,y) = \frac{|x-y|}{(n-1)}$
	- where $n$ is the number of possible values an attribute can take
	- for `educ_level`
		- $d(x,y) = \frac{|x-y|}{n-1} = \frac{|2-4|}{4-1}=\frac{2}{3}$
	- for `income` 
		- $d(x,y) = \frac{|x-y|}{n-1} = \frac{2-3}{3-1} = \frac{1}{2}$ 

### Dissimilarity → Interval or Ratio attribute
- **interval attributes** are numeric attributes where the diff between values are meaningful
	- there is a unit of measurement.
- **ratio attributes** are numeric attributes where both the differences between values and ratios are meaningful
	- a true absolute value exists (no negative values)
	- temp in Kelvin, counts, mass, length, etc.
- one of the widely used approaches for measuring dissimilarity of numeric attributes is using distance
	- $distance(x,y) = ||x-y||_{p}$
	- how we obtain the length of a certain vector

## Distance
- a distance (or metric) is a dissimilarity measure satisfying these three properties:
- **Positivity**:
	- $d(x,y) \geq 0, \text{for all }x \text{ and }y$
	- $d(x,y) = 0, \text{only if }x = y$
 - **Symmetry**:
	- $d(x,y) = d(y,x), \text{ for all }x \text{ and } y$
 - **Triangle Inequality**:
	- $d(x,z) \leq d(x,y) + d(y,z), \text{ for all }x \text{ and } y$
### Manhattan Distance or City Blo\ck Distance
- Given two vectors
	- $x = (x_1,...,x_k)$
	- $y=(y_1,...,y_k)$
- the manhattan distance is given by the following equation
- $d(x,y) = \sum\limits^{k}_{j=1}|x_j-y_j|$
### Euclidean Distance
- Given two vectors
	- $x = (x_1,...,x_k)$
	- $y=(y_1,...,y_k)$ 
- the Euclidean distance is given by the following equation
- $d(x,y) = \sqrt{\sum\limits^{k}_{j=1}(x_j-y_j)^{2}}$
### Minkowski Distance
- Given two vectors
	- $x = (x_1,...,x_k)$
	- $y=(y_1,...,y_k)$ 
- the Minkowski distance is given by the following equation
- $d(x,y) = \left(\sum\limits^{k}_{j=1}|x_j-y_j|^{p}\right)^{1/p}$

- is a generalization of the Manhattan and Euclidean Distances
- considered distance measure with some choices of p. Other choices of p may not actually yield a distance measure or metric
- distance measure or metric is essential as its properties are well-known and understood

## Loan Borrower Classification
- suppose we want to predict whether or not customer 5 will default or not if the following feature are known:
	- No, Single, 105,000, High 

dataset before pre-process

| ID  | Home Owner | Marital Status | Annual Income | Credit Limit | Defaulted |
| --- | ---------- | -------------- | ------------- | ------------ | --------- |
| 1   | Yes        | Single         | 125000        | High         | No        |
| 2   | No         | Married        | 100000        | Moderate     | No        |
| 3   | No         | Single         | 85000         | Low          | Yes       |
| 4   | No         | Divorced       | 95000         | Moderate     | Yes       |

### Step 1: Decide the number of nearest neighbors k
- choose an odd number due to the amount of classes to avoid ties
- since we have a very small data set, make nearest neighbors as few as possible
- for demonstration, we will use $k = 3$
### Step 2: Compute the distances
- notice that we have mixed attributes, so we have to deal with each of the features depending on its nature
	- Home Owner: Nominal
	- Marital Status: Nominal
	- Annual Income: Numeric (Ratio)
	- CC Limit: Ordinal
#### Step 2.a transform ordinal features to numerical encoding
- only the CC limit is ordinal, transform to numerical encoding
- nominal features do not need to be transformed
	- in IRL scenarios, nominal features may be pre-processed (one-hot encoding, etc.)
- normalize (min-max) numeric attributes for more straightforward calculation.

| ID  | Home Owner | Marital Status | Annual Income | Credit Limit | Defaulted |
| --- | ---------- | -------------- | ------------- | ------------ | --------- |
| 1   | Yes        | Single         | 1             | 3            | No        |
| 2   | No         | Married        | 0.375         | 2            | No        |
| 3   | No         | Single         | 0             | 1            | Yes       |
| 4   | No         | Divorced       | 0.25          | 2            | Yes       |
| 5   | No         | Single         | 0.5           | 3            | ?          |

#### Step 2.b select distance or metric to use
- we use euclidean