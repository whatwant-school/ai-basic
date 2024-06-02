# 3주차 - 기초 수학 첫걸음

## 경사하강법 (Gradient Descent) - 순한맛


### 미분 (differentiation)

- 변수의 움직임에 따른 함수값의 변화 측정

$$
f^\prime (x) = \lim_{h \to 0}{f(x + h) - f(x) \over h}
$$

```python
import sympy as sym
from sympy.abc import x

z = sym.diff(sym.poly(x**2 + 2*x + 3), x)

print(z)

###
Poly(2*x + 2, x, domain='ZZ')
```


### 경사상승법(gradient ascent)
- 미분값을 더해주며 함수의 극대값 위치를 구할 때 사용


### 경사하강법(gradient descent)
- 미분값을 뻬주며 함수의 극소값 위치를 구할 때 사용


### 편미분 (partial differentiation)

- 벡터가 입력인 다변수 함수의 경우 편미분을 사용
- 각 변수별로 편미분을 계산한 gradient vector를 이용하여 경사하강/상승법에 사용 가능

$$
\partial x_i \space f(x) = \lim_{h \to 0}{f(x + h e_i) - f(x) \over h} \\
\space \\
\nabla f = ( \partial x_1 f, \partial x_2 f, ... , \partial x_d f)
$$