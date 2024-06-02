# 3주차 - 기초 수학 첫걸음

## 벡터 (Vector)

- 1차원 배열로 선언하는 것은 보통 `행벡터` 이다.

$$
\mathbf{x} = \begin{bmatrix} 1 \\ 7 \\ 2 \end{bmatrix} , \quad
\mathbf{x}^T = \begin{bmatrix} 1,\ 7,\ 2 \end{bmatrix}
$$

```python
x = [1, 7, 2]
x = np.array([1, 7, 2])
```


### 덧셈 / 뺄셈

- 같은 모양일 때에만 가능

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ .\\.\\.\\ x_d  \end{bmatrix} , \quad
\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \\ .\\.\\.\\ y_d  \end{bmatrix} , \quad
\mathbf{x} \pm \mathbf{y} = \begin{bmatrix} x_1 \pm y_1 \\ x_2 \pm y_2 \\ .\\.\\.\\ x_d \pm y_d  \end{bmatrix}
$$


### 성분곱 (Fadamard product)

- 같은 모양일 때에만 가능

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ .\\.\\.\\ x_d  \end{bmatrix} , \quad
\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \\ .\\.\\.\\ y_d  \end{bmatrix} , \quad
\mathbf{x} \odot \mathbf{y} = \begin{bmatrix} x_1 y_1 \\ x_2 y_2 \\ .\\.\\.\\ x_d y_d  \end{bmatrix}
$$

```python
import numpy as np

x = np.array([1, 7, 2])
y = np.array([5, 2, 1])

z = x * y   ## 성분곱은 그냥 `*` 사용

print(z)

###
[ 5 14  2]
```


### 노름 (norm)

- 원점에서부터의 거리
- `norm`은 여러가지가 있으며, 보통 $ L_1, L_2 $ - norm 사용

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ .\\.\\.\\ x_d  \end{bmatrix} , \quad
\lVert \mathbf{x} \rVert _1 = \sum_{i=1}^d \lvert x _i \rvert , \quad
\lVert \mathbf{x} \rVert _2 = \sqrt{ \sum_{i=1}^d \lvert x _i \rvert ^2 }
$$

```python
def l1_norm(x):
  x_norm = np.abs(x)
  return np.sum(x_norm)

def l2_norm(x):
  x_norm = x * x
  x_norm = np.sum(x_norm)
  return np.sqrt(x_norm)

x = np.array([1, 7, 2])

print(l1_norm(x))
print(l2_norm(x))

###
10
7.3484692283495345
```


### 두 벡터 사이의 거리, 각도

- $ L_1, L_2 $ - norm을 이용해 두 벡터 사이의 거리 계산

$$
\lVert y - x \rVert = \lVert x - y \rVert
$$

- $ L_2 $ - norm을 이용해 두 벡터 사이의 `각도` 계산

$$
\lVert y - x \rVert _2 = \lVert x - y \rVert _2 \\
\space \\
\cos \theta = { \lVert x \rVert _2 ^2 + \lVert y \rVert _2 ^2 - \lVert x - y \rVert _2 ^2 \over 2 \lVert x \rVert _2 \lVert y \rVert _2 } \\
\space \\
\rightarrow \quad \cos \theta = { 2 \langle x, \space y \rangle \over 2 \lVert x \rVert _2 \lVert y \rVert _2 } \\
\space \\
\rightarrow \quad \cos \theta = { \langle x, \space y \rangle \over \lVert x \rVert _2 \lVert y \rVert _2 } \\
\space \\
\langle x, \space y \rangle = \sum_{i=1}^d x _i y _i \quad \leftarrow \text{내적 (inner product)}
$$


## 내적 (inner product)

- 내적은 `np.inner()`를 사용

```python
def angle(x, y):
  v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))
  return np.arccos(v)

x = np.array([1, 7, 2])
y = np.array([5, 2, 1])

print(angle(x, y))

###
1.0218962578343371
```

- 내적은 `정사영(orthogonal projection)`된 벡터의 길이와 관련
  - `Proj(x)`는 벡터y로 정사영된 벡터x의 그림자를 의미
  - 내적 = 정사영의 길이를 `벡터y`의 길이 $ \lVert y \rVert $ 만큼 조정한 값

$$
Proj(x) = \lVert x \rVert \space \cos \theta \\
\space \\
\langle x, \space y \rangle = \lVert x \rVert _2 \space \lVert y \rVert _2 \space \cos \theta
$$

- 내적은 두 벡터의 `유사도(similarity)`를 측정하는데에도 사용 가능
