# 3주차 - 기초 수학 첫걸음

## 행렬 (Matrix)

- 행렬(matrix)는 벡터를 원소로 가지는 `2차원 배열`
  - numpy에서는 `행(row)`이 기본 단위!

```python
import numpy as np

X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

print(X)

###
[[ 1 -2  3]
 [ 7  5  0]
 [-2 -1  2]]
 ```


### 표기법 (notation)
  - $ \mathbf{X} $ : 행렬 (matrix) - 대문자 볼드 X
  - $ \mathbf{x} _n $ : 벡터 (Vector) - 소문자 볼드 x
  - $ x _{nm} $ : 원소 (element) - 소문자 x

$$
\mathbf{X} =
\begin{bmatrix} \mathbf{x} _1 \\ \mathbf{x} _2 \\ .\\.\\.\\ \mathbf{x} _n  \end{bmatrix} =
\begin{bmatrix} x_{11} \quad x_{12} \quad ... \quad x_{1m} \\
                  x_{21} \quad x_{22} \quad ... \quad x_{2m} \\
                  .\\ x_{ij}\\.\\
                  x_{n1} \quad x_{n2} \quad ... \quad x_{nm} \end{bmatrix}
$$


### 전치행렬 (transpose matrix)

- 행과 열의 인덱스가 바뀐 행렬

$$
\mathbf{X} ^T =
\begin{bmatrix} x_{11} \quad x_{21} \quad ... \quad x_{n1} \\
                x_{12} \quad x_{22} \quad ... \quad x_{n2} \\
                .\\x_{ji}\\.\\
                x_{1m} \quad x_{2m} \quad ... \quad x_{nm} \end{bmatrix}
$$


### 행렬의 덧셈, 뺄셈, 성분곱, 스칼라곱

- 벡터의 연산과 동일


### 행렬 곱셈 (matrix multiplication)

- i번째 행벡터와 j번째 열벡터 사이의 내적
- 행렬곱은 X 열 갯수와 Y 행 개수가 같아야 함

$$
\mathbf{X}
= \begin{bmatrix} x_{11} \quad x_{12} \quad ... \quad x_{1m} \\
                  x_{21} \quad x_{22} \quad ... \quad x_{2m} \\
                  .\\.\\.\\
                  x_{n1} \quad x_{n2} \quad ... \quad x_{nm} \end{bmatrix} , \quad
\mathbf{Y}
= \begin{bmatrix} y_{11} \quad y_{12} \quad ... \quad y_{1l} \\
                  y_{21} \quad y_{22} \quad ... \quad y_{2l} \\
                  .\\.\\.\\
                  y_{m1} \quad y_{m2} \quad ... \quad y_{ml} \end{bmatrix} \\
  \space \\
\mathbf{XY} = \left( \sum_{k} x_{ik} \space y_{kj} \right) \neq \mathbf{YX}
$$

- numpy에서 행렬곱은 `@` 사용

```python
X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

Y = np.array([[0, 1],
              [1, -1],
              [-2, 1]])

Z = X @ Y

print(Z)

###
[[-8  6]
 [ 5  2]
 [-5  1]]
```


### numpy의 np.inner()

- 수학의 내적과는 다르게, i번째 행벡터와 j번째 행벡터 사이의 내적 계산

$$
\mathbf{X} =
\begin{bmatrix} x_{11} \quad x_{12} \quad ... \quad x_{1m} \\
                x_{21} \quad x_{22} \quad ... \quad x_{2m} \\
                .\\.\\.\\
                x_{n1} \quad x_{n2} \quad ... \quad x_{nm} \end{bmatrix} , \quad
\mathbf{Y} =
\begin{bmatrix} y_{11} \quad y_{12} \quad ... \quad y_{1m} \\
                y_{21} \quad y_{22} \quad ... \quad y_{2m} \\
                .\\.\\.\\
                y_{n1} \quad y_{n2} \quad ... \quad y_{nm} \end{bmatrix} \\
\space \\
\mathbf{X Y^T} = \left( \sum_{k} x_{ik} \space y_{jk} \right)
$$

```python
X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

Y = np.array([[0, 1, -1],
              [1, -1, 0]])

Z = np.inner(X, Y)

print(Z)

###
[[-5  3]
 [ 5  2]
 [-3 -1]]
 ```


### 행렬을 이해하는 다른 방법

- 행렬은 벡터공간에서 사용되는 연산자(operator)로 이해

$$
z_i = \sum_{j} a_{ij} \space x_{j} \\
\space \\
\begin{bmatrix} z_{1} \\
                z_{2} \\
                .\\.\\.\\
                z_{n} \end{bmatrix} =
\begin{bmatrix} a_{11} \quad a_{12} \quad ... \quad a_{1m} \\
                a_{21} \quad a_{22} \quad ... \quad a_{2m} \\
                .\\.\\.\\
                a_{n1} \quad a_{n2} \quad ... \quad a_{nm} \end{bmatrix}
\begin{bmatrix} x_{1} \\
                x_{2} \\
                .\\.\\.\\
                x_{n} \end{bmatrix}
$$


### 역행렬 (inverse matrix)

- 어떤 행렬 A의 연산을 거꾸로 되돌리는 행렬 = $ \mathbf{A} ^{-1} $
- 행과 열의 숫자가 같고, 행렬식(determinant)이 0이 아닌 경우에만 계산 가능

```python
X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

X_inv = np.linalg.inv(X)

Z = X @ X_inv  # 대각선의 값이 1이 나오고 나머지는 0에 가까운 값이 나온다

print(X_inv)
print(Z)

###
[[ 0.21276596  0.0212766  -0.31914894]
 [-0.29787234  0.17021277  0.44680851]
 [ 0.06382979  0.10638298  0.40425532]]
[[ 1.00000000e+00 -1.38777878e-17  0.00000000e+00]
 [-2.22044605e-16  1.00000000e+00 -5.55111512e-17]
 [-2.77555756e-17  0.00000000e+00  1.00000000e+00]]
```


### 항등 행렬 (identity matrix) = 단위 행렬 (unit matrix)

$$
\mathbf{A} \mathbf{A} ^{-1} = \mathbf{A} ^{-1} \mathbf{A} = \mathbf{I} \\
\space \\
\begin{bmatrix} 1 \quad 0 \quad ... \quad 0 \\
                0 \quad 1 \quad ... \quad 0 \\
                .\\
                0 \quad 0 \quad ... \quad 1 \end{bmatrix}
$$


### 무어-펜로즈(Moore-Penrose) 역행렬

- 역행렬을 구할 수 없으면, 유사-역행렬(pseudo-inverse) 또는 무어-펜로즈(Moore-Penrose) 역행렬 $ \mathbf{A} ^+ $ 를 이용

$$
\begin{cases}
\text{n} \ge \text{m 인 경우,} \quad  \mathbf{A} ^+ = ( \mathbf{A} ^T \mathbf{A} ) ^{-1} \mathbf{A} ^T \\
\space \\
\text{n} \le \text{m 인 경우,} \quad  \mathbf{A} ^+ = \mathbf{A} ^T ( \mathbf{A} \mathbf{A} ^T ) ^{-1}\\
\end{cases}
$$

- numpy에서는 `np.linalg.pinv()`(pseudo-invert)를 이용

```python
Y = np.array([[0, 1],
              [1, -1],
              [-2, 1]])

Y_pinv = np.linalg.pinv(Y)  # 행과 열의 개수가 다르기에 역행렬을 못구하는 경우지만, 유사 역행렬 계산

Z = Y_pinv @ Y

print(Y_pinv)
print(Z)

###
[[ 5.00000000e-01  4.09730229e-17 -5.00000000e-01]
 [ 8.33333333e-01 -3.33333333e-01 -1.66666667e-01]]
[[ 1.00000000e+00 -2.22044605e-16]
 [ 0.00000000e+00  1.00000000e+00]]
```


### 유사-역행렬을 이용한 연립 방정식 풀기

- `np.linalg.pinv()`를 이용하면 해를 구할 수 있음

$$
a_{11} x_1 + a_{12} x_2 + ... + a_{1m} x_m = b_1 \\
a_{21} x_1 + a_{22} x_2 + ... + a_{2m} x_m = b_2 \\
.\\.\\.\\
a_{n1} x_1 + a_{n2} x_2 + ... + a_{nm} x_m = b_n \\
\space \\
\text{n} \le \text{m 인 경우, 식이 변수 개수보다 작거나 같아야 함}
$$

- 풀어보면,

$$
\rightarrow \mathbf{Ax} = \mathbf{b} \\
\space \\
\Rightarrow \quad
\begin{split}
\mathbf{x} &= \mathbf{A} ^+ \space \mathbf{b} \\
&= \mathbf{A} ^T ( \mathbf{A} \mathbf{A} ^T ) ^{-1} \space \mathbf{b}
\end{split}
$$


### 유사-역행렬을 이용한 선형회귀분석

- `np.linalg.pinv()`를 이용하면 데이터를 선형모델(linear model)로 해석하는 선형회귀식을 찾을 수 있음

$$
\begin{bmatrix} x_{11} \quad x_{12} \quad ... \quad x_{1m} \\
                x_{21} \quad x_{22} \quad ... \quad x_{2m} \\
                .\\.\\.\\
                x_{n1} \quad x_{n2} \quad ... \quad x_{nm} \end{bmatrix}
\begin{bmatrix} \beta_{1} \\
                \beta_{2} \\
                .\\.\\.\\
                \beta_{m} \end{bmatrix} \ne
\begin{bmatrix} y_{1} \\
                y_{2} \\
                .\\.\\.\\
                y_{m} \end{bmatrix} \\
\space \\
\mathbf{X} \beta = \hat{\mathbf{y}} \approx \mathbf{y} \\
\space \\
\Rightarrow \quad
\begin{split}
\beta &= \mathbf{X} ^+ \space \mathbf{y} \\
&= ( \mathbf{X} ^T \mathbf{X} ) ^{-1} \space \mathbf{X} ^T \mathbf{y}
\end{split}
$$


### 선형회귀분석
- sklearn의 LinearRegression과 같은 결과를 가져올 수 있다.