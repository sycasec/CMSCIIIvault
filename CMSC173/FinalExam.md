# Final Exam
## Part I
1. Suppose you toss a fair coin eight times. Which one(s) would most likely occur among the sequences below? (2 pts) (i) HHHHHHHH (ii) HHTHTHHT (iii) HHHHTTTT (iv) HTTHTHHT a) (iv) b) (iii) and (iv) c) (ii), (iii), and (iv) d) All are equally likely. answer d
2. Suppose 𝐴 and 𝐵 are dependent events. Let 𝑃(𝐴) be the probability that 𝐴 occurs, 𝑃(𝐴 ∩ 𝐵) be the probability that 𝐴 and 𝐵 occur, and 𝑃(𝐴|𝐵) be the probability that 𝐴 occurs given 𝐵 has occurred. Which of the following options is the most accurate statement? (2 pts) a) 𝑃(𝐴 ∩ 𝐵) and 𝑃(𝐴|𝐵) are always less than or equal to 𝑃(𝐴) b) 𝑃(𝐴 ∩ 𝐵) is always less than or equal to 𝑃(𝐴|𝐵) and 𝑃(𝐴) c) 𝑃(𝐴 ∩ 𝐵) and 𝑃(𝐴) answer d
3. The distribution of scores in a particular exam resulted in a left-skewed distribution. Which of the following is the most accurate statement? (2 pts) a) The exam is likely difficult. b) The exam is likely just at the appropriate difficulty. c) The exam is likely easy. d) There is not enough information to infer about the difficulty of the exam answer c
## Part II
### 1.Consider a hypothetical situation where machine learning algorithms surpass human intelligence in every measurable aspect. In this extraordinary era of hyperintelligence, what role, if  any, remains for humanity? Explain. (2 pts)
Answer: This is also known as the technological singularity, a hypothetical future point in time at which technological growth is already beyond the control of humanity, and nowadays used as a fearmongering tactic to get views on youtube or gain religious cult-like authority. Artificial Super Intelligence, beyond just general intelligence, according to Stephen Hawking could lead to the inevitable doom of humanity. Hyperintelligent AI potentially would no longer need humans and thus eliminate humanity for access to scarce resources. These hypotheses are equally valid because we have no idea what will happen in this scenario - the nature of hyperintelligence is that it is beyond human understanding. Assuming that humanity somehow, miraculously manages to retain control over this godlike intelligent AI, whoever has control of the AI has control over the entirety of humanity. The only scenario that would play out “good enough” is when this hyperintelligent AI is used for the benefit of the entirety of humanity. Apart from this specific scenario, is a massive forking branch of scenarios that could lead to the end of humanity. 
### 2. Machine learning thrives on data, and data thrives on labels. But what happens when the very act of labeling the world shapes our perception of it in unexpected ways? Discuss the potential biases and unintended consequences of training machines on data imbued with human subjectivity, social constructs, etc. (2 pts)
Answer: Tay, one of the very first AI chatbots released in the internet and on twitter no less, was created by microsoft in 2016. Trained on twitter data, Tay eventually started releasing racist and sexually-charged messages in response to Twitter users. When AI is trained on data heavily charged with human subjectivity and social constructs without appropriate pre-processing and cleaning, we get horrendously irresponsible models. This is not just a problem of developing AI, but a problem with humanity as a whole. This leads us to meaningful questions on society, morality, ethics, and philosophy, some of the many things we need to improve upon as humans to truly understand the nature of reality. By improving our understanding of the world around us, we gather and label data in superior methodologies to improve our AI models. 
### 3. Illustrate a situation where the Manhattan distance results in a different classification than the Euclidean distance when using the k-nearest neighbors (KNN) algorithm. Assume that all other parameters are the same. Create a small toy dataset for illustration and justify why this happens in general. (2 pts)
Ans: This usually happens because the Manhattan distance only counts distance in terms of the x and y axes which means that if the points are at a diagonal from the target point, they have more distance than a point which lies directly vertical or horizontal from them which is already accounted for by Euclidean distance.
-  ![[Pasted image 20231220012239.png|395]]  

## Part III
### Problem 1
a) ![[Pasted image 20231219180419.png|525]]
b) ![[Pasted image 20231219180733.png]]
c) $\frac{5}{10} = \frac{1}{2}$
d) $\frac{10}{20} = \frac{1}{2}$
e)
- $\vec{x}^{21} = (1,122,200,0,1)$
- $P(trestbps=122|t=0) = N(\mu_{trestbps}, \sigma_{trestbps}^2)$
- relative likelihood $t=0$
	- $p_{trestbps}(x=122|0)=\frac{1}{\sigma_{trestbps|0}\sqrt{2\pi}}exp\left[-\frac{1}{2}\left(\frac{x-\mu_{trestbps|0}}{\sigma_{trestbps|0}}\right)^{2}\right]$
- ![[Pasted image 20231219202449.png]]
### Problem 2
a) Suppose 𝑘 = 5, and we use the Manhattan distance as our metric. What would # be the assigned class of the same unlabeled sample 𝑥 = (1, 122, 200,0,1)? Answer = 0
b) What would be the class assignment of 𝑥 if we use the Euclidean distance as # the metric? Assume that all other parameter configurations are the same. Answer = 1
c) If the results of items (a) and (b) differ, which of the two distance metrics yields # the same class assignment as the Naïve Bayes method in item # 1? # Answer = manhattan
### Problem 3
- ![[Pasted image 20231219161728.png|700]]

a) ![[Pasted image 20231219194151.png|550]]
b) ![[Pasted image 20231219202307.png|500]]

c) ![[Pasted image 20231219202324.png]]