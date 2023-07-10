# Logistic Regression - Week 1

```toc
```

## Binary Classification
- recognizes output as 1 or 0 (can only be one of either, hence binary).

### Notation
$$
(x,y)
$$
where:
$$
x\in\mathbb{R}^{n_{x}}::y\in{0,1}
$$
$$
trainingSamples = \{(x^1y^1),(x^2y^2),(x^{m}y^{m})\}
$$

## Application
Given $x$, we want $\hat{y}-P(y=1|x)$ , $0 \leq \hat{y} \leq 1$ 
**Parameters**: $w\in\mathbb{R}^{n_{x}}, b\in\mathbb{R}$
**Output**: $\hat{y} = \sigma(w^Tx+b)$
where: $$\sigma(z)=\frac{1}{1+e^{-z}}$$
![[Pasted image 20221216110229.png|425]]

**Loss (error) Function**
$$L(\hat{y},y) = y\log\hat{y}+(1-y)\log(1-\hat{y})$$
**Cost Function**
$$J(w,b) = \frac{1}{m}\sum_{i=1}^{m}L(\hat{y}^{i},y^{i})$$

## Gradient Descent
![[Pasted image 20221216112237.png|275]]

to decrease or *apply J(w)*,
Repeat {
	$$w := w - \alpha \frac{\partial{J(w)}}{\partial{w}}$$
}
where $\alpha$ is a learning rate.