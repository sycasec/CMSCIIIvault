# Midterm Examination

## Part I
### Q1
According to the following data table, which variable(s) is(are) categorical?

| Age | Sex    | Weight | Ethnicity |
| --- | ------ | ------ | --------- |
| 23  | Male   | 180    | 1         |
| 18  | Female | 126    | 0         |
| 20  | Female | 139    | 2         |
| 19  | Male   | 154    | 1         |
| 20  | Male   | 202    | 3         |

a. Sex OR b. Sex and Ethnicity? di ko sure

### Q2
- the data in the table represents:
	- the amount of raw material in tons put into an injection machine each day *var x*
	- the amount of scrap plastic in tons every four weeks *var y*
- A scatterplot of the data confirms that there is a linear association. 
	- Report the equation for predicting scrap from raw material using words such as scrap, not x and y. 
	- State the slope and intercept of the prediction equation. 
	- Round all calculations to the nearest hundredth. (1 pt)

| x     | y    |
| ----- | ---- |
| 2.71  | 3.61 |
| 2.33  | 2.80 |
| 2.33  | 2.77 |
| 2.221 | 2.34 |
| 2.11  | 2.15 |
| 2.08  | 2.06 |
| 1.98  | 2.02 |
| 1.95  | 1.95 |
| 1.84  | 1.73 |
| 1.84  | 1.68 | 

LinReg
$y = a + bx$
$a = 2.376991175$
$b = 2.192699333$
$r^{2}= 0.9806834986$
$r = 0.9902946524$

|              | Coefficients |
| ------------ | ------------ |
| Intercept    | -2.376991175 |
| X Variable 1 | 2.192699333  | 

c. scrap = -2.38 + 2.19(raw material); slope = 2.19 and the intercept is -2.38.
according to chatgpt hahaahah
### Q3
The variables temperatures and monthly ice cream sales were collected for a machine learning project. Which variable should be the feature, and which should be the target?

a. *Temperature* is the feature and *ice cream sales* is the target because a city's
**temperature** could explain the amount of **ice cream sales.**

## Part II
### Q1
nominal
### Q2
binary outcome variables
### Q3
True ?? di ko sure
### Q4
True
### Q5
True
### Q6
False ? wa ko kibaw

## Part III
### Q1
The following linear regression model can be used to predict ice cream sales at a popular ice cream shop:
$sales\ per\ hour = -631.25 + 11.25 \times (current\ temperature\ in \degree F)$
Discuss why or why not this equation has a reasonable interpretation.

The given model’s $b_0$ implies negative sales at zero degrees Fahrenheit, which may be inadequate as you cannot have negative sales. The model also assumes a linear relationship with temperature and sales at the slope of 11.25. While it would be intuitive to expect an increase of sales with rising temperature and vice versa, this model reduces ice cream sales patterns to a mere correlation and is rather unreasonable. A more realistic model would incorporate time of day, season such as in the summer, promotional events such as buy 1 take 1, etc. 
### Q2
Logistic Regression models the log-odds of a binary outcome assuming a linear relationship between features and log-odds. It provides interpretable coefficient values and is suitable for when understanding the impact of features is necessary. Naive Bayes’ on the otherhand assumes  the conditional independence of features and is more effective in datasets with many features as compared to Logistic Regression. 
### Q3
By improving upon our laws that regulate the usage of classification algorithms in business practices, we can ensure a legal and ethical basis on using automated decision making on highly sensitive factors that directly affect people’s lives. However, educating the general public on the nature of artificial intelligence and how large corporations use it in ways that directly affects the lives of the average consumer is the only way forward where we ensure human autonomy is not undermined. With this, we can ensure that questions and concerns regarding ethical use can be raised. We can have more people implement AI accountability, audits and assessments, bias mitigation, ensuring that human rights are protected moving forward.
### Q4
Due to the nature of AI and by extension classification algorithms, established practices in education, criminal justice, and healthcare will be followed ensuring a *conservative* system as in one that follows old practices. This can reveal biases in established practices, allowing us to improve upon established systems. However, this can also lead to unfair treatment if no audit or accountability measures are set in place.
### Q5
A straightforward way of ensuring fairness in machine learning systems is through audit or accountability laws and data diversity improvement. However, I would argue that removing bias is more of an ethical or philosophical problem, as “removing a bias” can instead introduce a bias into the model, giving it a target that is biased towards whatever outcome is desired. By continually improving our understanding of ethics, policies, and by improving our society as a whole, we can hope to improve the quality of data we put into our machine learning systems.
## Part IV
### Q1
A company is considering launching a new product. It has collected data on the number of units sold (Y) and the amount spent on advertising X in dollars for similar products in the past, as shown in the table below.

| X   | Y   |
| --- | --- |
| 6   | 105 |
| 35  | 117 |
| 77  | 128 |
| 4   | 101 |
| 27  | 113 |
| 7   | 104 |
| 16  | 106 |
| 61  | 123 |
| 14  | 103 |
| 84  | 138 |
| 91  | 132 |
| 30  | 108 |
| 72  | 129 |
| 12  | 108 |
| 77  | 128 |
| 80  | 130 |
| 4   | 95  |
| 48  | 108 |
| 90  | 143 |
| 95  | 137 | 

#### a
determine the simple linear regression equation that best fits the data
$\hat{y} = 99.0233 + 0.4038 \cdot x$ 
#### b
draw a scatter plot representing the relationships in the tabulated data. Include the regression line in the plot
(*ako i suwat sa paper kay y=99.0233 diri kay na wrong man*)
![[Pasted image 20231122193300.png|350]]

#### c 
What would be the expected number of units sold if the company does not spend anything on advertising?

If the company does not spend on anything advertising $(X = 0)$,
$\hat{y} = b_0 +b_{1}\cdot x$
$\hat{y} = 99.0233 + 0.4038 \cdot 0$
$\hat{y} = 99.0233$
#### d 
$\hat{y} = b_0 +b_{1}\cdot x$
$\hat{y} = 99.0233 + 0.4038 \cdot 50$
$\hat{y} = 99.0233 + 20.19$
$\hat{y} = 119.2133$
#### e
$\hat{y} = b_0 +b_{1}\cdot x$
$\hat{y} = 99.0233 + 0.4038 \cdot 1000$
$\hat{y} = 99.0233 + 403.8$
$\hat{y} = 502.8233$

### Q2
An online store is trying to develop a model to predict whether a new customer will buy a product based on data from a sample of 14 randomly selected customers. The store uses four features as its predictors: (i) age, (ii) maximum credit card limit, (iii) whether employed or not, and (iv) sex. The data for the sampled customers is depicted in the table below:

I have turned feature Age “young”, “middle”, “old” to -1, 0, 1
I have turned feature Credit Limit “low”, “moderate”, “high” to -1, 0, 1
I have turned feature Employed “yes”, “no” to 0, 1
I have turned feature Sex “Male”, “Female” to 0, 1
I have turned class Buy “yes”, “no” to 0, 1

| Customer No. | Age | Credit Limit | Employed | Sex | Buy |
| ------------ | --- | ------------ | -------- | --- | --- |
| 1            | 0   | -1           | 0        | 0   | 0   |
| 2            | 0   | -1           | 0        | 1   | 0   |
| 3            | -1  | -1           | 0        | 0   | 1   |
| 4            | 1   | 0            | 0        | 0   | 1   |
| 5            | 1   | 1            | 1        | 0   | 1   |
| 6            | 1   | 1            | 1        | 1   | 0   |
| 7            | -1  | 1            | 1        | 1   | 1   |
| 8            | 0   | 0            | 0        | 0   | 0   |
| 9            | 0   | 1            | 1        | 0   | 1   |
| 10           | 1   | 0            | 1        | 0   | 1   |
| 11           | 0   | 0            | 1        | 1   | 1   |
| 12           | -1  | 0            | 0        | 1   | 1   |
| 13           | -1  | -1           | 1        | 0   | 1   |
| 14           | 1   | 0            | 0        | 1   | 0   |

#### a
Draw a histogram for each attribute (including the class). Label each histogram properly. Briefly interpret the pattern that you observe in each histogram.

![[Pasted image 20231122204047.png]]
#### b
probability table
![[Pasted image 20231122203834.png|475]]

#### c
Using naïve Bayes, what is the probability that a randomly selected customer’s credit limit was low given that they bought the product, or P(Credit Limit = Low| Buy = yes)? Do not perform any Laplace smoothing.
- $\frac{2}{9}$

#### d 
What is the prior probability that a customer buys a product? Do not perform any Laplace smoothing
- $\frac{9}{14}$
#### e
Suppose we have a new customer with the following attributes: Age = middle, Credit Limit - high, Employed = no, Sex = female. Using naive Bayes, calculate the posterior probability that a customer buys the product given the data. Do not perform any Laplace smoothing
$\vec{x}^{15} = (0,1,0,1,?)$

##### proportional probability 
$P(buy=1|\vec{x}^{15}) = (\frac{2}{9})(\frac{3}{9})(\frac{3}{9})(\frac{3}{9})\left(\frac{9}{14}\right) \propto 0.005 291 005 291$

$P(buy=0|\vec{x}^{15}) = (\frac{3}{5})(\frac{1}{5})(\frac{4}{5})(\frac{3}{5})\left(\frac{5}{14}\right) \propto 0.02057142857$
##### posterior probability
$P(\vec{x}^{15}) = 0.005 291 005 291 + 0.02057142857 = 0.025 862 433 86$
$P(buy=1|\vec{x}^{15})= \frac{0.005 291 005 291}{0.025 862 433 86} = 0.204 582 651 4 \approx 0.2046$
$P(buy=0|\vec{x}^{15})=\frac{0.02057142857}{0.025 862 433 86}= 0.795 417 348 6 \approx 0.7954$

##### final answer
posterior probability that customer buys the product given data: $\vec{x}^{15} = (0,1,0,1,?)$
$P(buy=1|\vec{x}^{15})= \frac{0.005 291 005 291}{0.025 862 433 86} = 0.204 582 651 4 \approx 0.2046 = 20.46\%$
### Q3
Apple and Samsung sometimes launch similar products in the same business period. The events 𝐴 and 𝐵 are defined as follows:
𝐴 = the event that Apple launches a product. 
𝐵 = the event that Samsung launches a product.

Given
$P(A) = 0.25$
$P (A \cap B) = 0.15$
$P(A' \cap B') = 0.17$
(note that 𝐴 ′ is the complement of 𝐴)

answer the following:

#### a 
Find the probability that Samsung will launch a product on a randomly selected business period. 
since we can calculate $P(A \cup B)$ with
$P(A \cup B) = 1 - P(A' \cap B')$,
$P(A \cup B) = 1 - 0.17$,
$P(A \cup B) = 0.83$,
then,
$P(B) = P(A \cup B) - P(A) + P(A \cap B)$
$P(B) = 0.83 - 0.25 + 0.15$
$P(B) = 0.73$
#### b
Find the probability that Samsung will launch a product given that Apple launched a product.
$P(B|A) = \frac{P(A \cap B)}{P(A)}$
$P(B|A) = \frac{0.15}{0.25}$
$P(B|A) = 0.6$
#### c
Determine if 𝐴 and 𝐵 are independent events
$A \coprod B$ if and only if:
$P(A \cap B) = P(A) \cdot P(B)$
$0.15 =? (0.25) \cdot (0.73)$
$0.15 \neq 0.1825$

therefore, they are not independent.