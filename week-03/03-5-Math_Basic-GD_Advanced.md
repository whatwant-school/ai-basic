# 3주차 - 기초 수학 첫걸음

## 경사하강법 (Gradient Descent) - 매운맛


### 경사하강법으로 선형회귀 계수 구하기

- 선형회귀 목적식 = $ \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 $
- → 이를 최소화 하는 $ \beta $ 를 찾아야 함

$$
\nabla _\beta \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 =
( \partial \beta _1 \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2, \space ... , \space \partial \beta _d \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 ) \\
\space \\
\partial \beta _k \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 = \partial \beta _k
\begin{Bmatrix}
{1 \over n} \sum \limits _{i=1}^n (y_i - \sum \limits _{j=1}^d \mathbf{X} _{ij} \beta _j ) ^2
\end{Bmatrix} ^{1 \over 2} \\
\space \\
= - {\mathbf{X} _k^T (\mathbf{y} - \mathbf{X} \beta) \over n \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2}
\space \\
\space \\
\partial \beta \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 = 
( \partial \beta _1 \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2, \space ... , \space \partial \beta _d \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2 )
\\
\space \\
= - {\mathbf{X} ^T (\mathbf{y} - \mathbf{X} \beta) \over n \lVert \mathbf{y} - \mathbf{X} \beta \rVert _2}
$$

- 목적식을 최소화하는 $ \beta $ 를 구하는 경사하강법 알고리즘은 다음과 같다.

$$
\beta ^{(t+1)} \leftarrow \beta ^{(t)} - \lambda \nabla \beta \lVert \mathbf{y} - \mathbf{X} \beta ^{(t)} \rVert \\
\space \\
\beta ^{(t+1)} \leftarrow \beta ^{(t)} + {2 \lambda \over n } \mathbf{X} ^T (\mathbf{y} - \mathbf{X} \beta ^{(t)} ) \\
$$


### 확률적 경사하강법 (Stoochastic Gradient Descent, SGD)

- 데이터 한개 또는 일부(mini-batch)만 활용하여 업데이트
  - 딥러닝의 경우 SGD가 GD보다 실증적으로 더 낫다고 검증되었음





