# 5주차 - 딥러닝 핵심 기초

# Linear Regression

## Data definition

$$
X_{train} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
\quad
Y_{train} = \begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}
$$

```python
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
```


## Hypothesis (가설, 추정)

- W : Weight
- b : bias

$$
y = Wx + b
$$

```python
W = torch.zeros(1, requires_grad = True)  # requires_grad = True : 학습할 것이라고 명시
b = torch.zeros(1, requires_grad = True)

hypothesis = W * x_train + b
```


## Mean Squared Error (MSE)

- $H(x^{(i)})$ : Prediction
- $y^{(i)}$ : Target

$$
cost(W,\ b) = {1 \over m}\ \sum\limits_{i=1}^m (H(x^{(i)}) - y^{(i)})^2
$$

```python
cost = torch.mean((hypothesis - y_train) ** 2)
```


## Gradient descent

- torch.optim 라이브러리 사용
- 항상 붙어다니는 3줄
  - zero_grad() : gradient 초기화
  - backward() : gradient 계산
  - step() : 개선 (gradient descent)

```python
optimizer = torch.optim.SGD([W, b], lr=0.01)

optimizer.zero_grad()
cost.backward()
optimizer.step()
```