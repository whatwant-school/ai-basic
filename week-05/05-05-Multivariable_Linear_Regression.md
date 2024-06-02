# 5주차 - 딥러닝 핵심 기초

# Multivariable Linear Regression
- https://github.com/deeplearningzerotoall/PyTorch


## Hypothesis Function

- 입력변수가 3개라면 weight도 3개

$$
H(x) = Wx + b \\
\space \\
H(x) = w_1 x_1 + w_2 x_2 + w_3 x_3 + b
$$


## Cost Function: MSE

- 기존 Simple Linear Regression과 동일한 공식

$$
cost(W,\ b) = {1 \over m}\ \sum\limits_{i=1}^m (H(x^{(i)}) - y^{(i)})^2
$$