# 5주차 - 딥러닝 핵심 기초

# Gradient Descent

## Hypothesis (Linear Regression)

$$
H(x) = Wx + b
$$

```python
W = torch.zeros(1, requires_grad = True)
b = torch.zeros(1, requires_grad = True)

hypothesis = W * x_train + b
```


## Simpler Hypothesis Function

$$
H(x) = Wx
$$

```python
W = torch.zeros(1, requires_grad = True)

hypothesis = W * x_train
```

## Dummy Data

```python
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])
```

## What is the best model ?

- $H(x) = x$가 정확한 모델
- $W = 1$이 가장 좋은 숫자


## Cost function: Intuition (직관, 직감)

- $W=1$일 때 $cost = 0$
- 1에서 멀어질 수록 높아진다

$$
cost(W,\ b) = {1 \over m}\ \sum\limits_{i=1}^m (H(x^{(i)}) - y^{(i)})^2
$$

```python
cost = torch.mean((hypothesis - y_train) ** 2)
```


## Gradient Descent

$$
{\partial {cost} \over \partial W} = \nabla W \\
\space \\
\space \\
cost(W) = {1 \over m}\ \sum\limits_{i=1}^m (Wx^{(i)} - y^{(i)})^2 \\
\space \\
\nabla W = {\partial {cost} \over \partial W} = {2 \over m}\ \sum\limits_{i=1}^m (Wx^{(i)} - y^{(i)})\ x^{(i)} \\
\space \\
\space \\
W :\ = W - \alpha\ \nabla W
$$

```python
gradient = 2 * torch.mean((W * x_train - y_train) * x_train)

lr = 0.1
W -= lr * gradient
```


## Gradient Descent with torch.optim

- torch.optim으로 gradient descent 구현 가능

```python
optimizer = torch.optim.SGD([W], lr=0.15)

optimizer.zero_grad()
cost.backward()
optimizer.step()
```