# 5주차 - 딥러닝 핵심 기초

# Logistic Regression


## Hypothesis Function

$$
H(x) = { 1 \over 1 + e^{- W^T X}}
$$


## Cost Function

- if $y \simeq H(x)$, cost is near 0
- if $y \neq H(x)$, cost is high

$$
cost(W) = - {1 \over m} \sum y\ log(H(x)) + (1 - y)(log(1 - H(x))
$$


## Weight Update via Gradient Descent

- $\alpha$ : Learning Rate

$$
W := W - \alpha {\partial \over \partial W} cost(W) = W - \alpha\ \nabla_W \ cost(W)
$$