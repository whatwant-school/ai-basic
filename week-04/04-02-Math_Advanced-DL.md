# 4주차 - 기초 튼튼, 수학 튼튼

## 딥러닝 학습방법 이해하기 (Mathmatics for Artificial Intelligence)

### 선형모델

$$
\begin{bmatrix} \mathbf{o}_{1} \\
                \mathbf{o}_{2} \\
                .\\.\\.\\
                \mathbf{o}_{n} \end{bmatrix}
\quad = \quad
\begin{bmatrix} \mathbf{x}_{1} \\
                \mathbf{x}_{2} \\
                .\\.\\.\\
                \mathbf{x}_{n} \end{bmatrix} \space
\begin{bmatrix} w_{11} \quad w_{12} \quad ... \quad w_{1p} \\
                w_{21} \quad w_{22} \quad ... \quad w_{2p} \\
                .\\.\\.\\
                w_{d1} \quad w_{d2} \quad ... \quad w_{dp} \end{bmatrix}
\space + \space
\begin{bmatrix} b_{1} \quad b_{2} \quad ... \quad b_{p} \\
                b_{1} \quad b_{2} \quad ... \quad b_{p} \\
                .\\.\\.\\
                b_{1} \quad b_{2} \quad ... \quad b_{p} \end{bmatrix} \\
\space \\
\begin{matrix}
\mathbf{O} \quad &=& \quad \quad \mathbf{X} \quad \quad \quad \mathbf{W} \quad \quad &+& \quad \quad \mathbf{b} \quad \\
(n \times p) \quad &=& \quad (n \times d) \quad (d \times p) \quad &+& \quad (n \times p)
\end{matrix}
$$


### softmax

- 모델의 출력을 확률로 해석할 수 있게 변환해주는 연산

$$
\text{softmax}(\mathbf{o}) = \left( { \text{exp}(o_1) \over \sum\limits_{k=1}^p \text{exp}(o_k) } \space , \space ... \space , { \text{exp}(o_p) \over \sum\limits_{k=1}^p \text{exp}(o_k) } \right)
$$

```python
def softmax(vec):
  denumerator = np.exp(vec - np.max(vec, axis=-1, keepdims=True))  # overflow 방지 구문
  numerator = np.sum(denumerator, axis=-1, keepdims=True)
  return denumerator / numerator

vec = np.array([[1, 2, 0], [-1, 0, 1], [-10, 0, 10]])
softmax(vec)

###
array([[2.44728471e-01, 6.65240956e-01, 9.00305732e-02],
       [9.00305732e-02, 2.44728471e-01, 6.65240956e-01],
       [2.06106005e-09, 4.53978686e-05, 9.99954600e-01]])
```


### 신경망 (Neural Network)

- 신경망은 선형모델과 활성함수(activation function)를 합성한 함수
- 다층 퍼셉트론 (Multi-Layer Perceptron, MLP) = 신경망이 여러층 합성된 함수

$$
\mathbf{H} = ( \sigma (\mathbf{z}_1), \space ... \space , \sigma (\mathbf{z}_n) ) \\
\space \\
\sigma (\mathbf{z}) = \sigma (\mathbf{Wx} + \mathbf{b})
$$


### 활성함수 (Activation Function)

- 비선형(nonlinear) 함수


### 순전파 (Forward Propagation)

- 순차적인 신경망 계산


### 역전파 (Backpropagation)

- 연쇄법칙(chain-rule)기반 자동미분(auto-differentiation)을 사용해 Gradient Vector를 전달

$$
z = {(x + y)}^2 \\
\space \\
z = w^2 \quad \implies \quad { \partial z \over \partial w } = 2 w \\
\space \\
w = x + y \quad \implies \quad { \partial w \over \partial x } = 1 , \quad { \partial w \over \partial y } = 1 \\
\space \\
{ \partial z \over \partial x } \space = \space { \partial z \over \partial w } { \partial w \over \partial x } \space = \space 2w \cdot 1 \space = \space 2(x + y)
$$
