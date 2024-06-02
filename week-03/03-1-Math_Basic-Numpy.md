# 3주차 - 기초 수학 첫걸음

## Numpy

- 참고 자료: https://github.com/TEAMLAB-Lecture/AI-python-connect/

### ndarray (Numpy Dimension Array)
- Numpy의 가장 기본이 되는 데이터 단위
- Numpy에서는 `Dynamic Typing`을 지원하지 않음

```python
import numpy as np

test_array = np.array(["1", "4", 5, 8], float)

print(test_array)
print(type(test_array))
print(type(test_array[3]))

###
[1. 4. 5. 8.]
<class 'numpy.ndarray'>
<class 'numpy.float64'>
```

- 대용량 데이터를 다루는 경우 `float64`는 너무 큰 용량일 수 있음

```python
test_array = np.array([[[1, "8"],[2, "8"],[3, "8"]],
                       [[4, "8"],[5, "8"],[6, "8"]],
                       [[7, "8"],[8, "8"],[9, "8"]],
                       [[0, "8"],[1, "8"],[2, "8"]]], np.float32)

print(test_array.dtype)  # ndarray 전체의 데이터 Type을 반환
print(test_array.shape)  # ndarray shape을 반환 
print(test_array.ndim)   # number of dimension
print(test_array.size)   # number of data

###
float32
(4, 3, 2)
3
24
```


### reshape
- element 개수는 동일해야 함
- 1-dim으로 하고자 할 때엔 `flatten()`을 사용할 수도 있음

```python
test_matrix = [[1,2,3,4], [5,6,7,8]]

print(np.array(test_matrix).shape)
print(np.array(test_matrix).reshape(2,2,2))
print(np.array(test_matrix).reshape(8,).shape)
print(np.array(test_matrix).reshape(-1,2).shape)  # -1 : size를 기반으로 row 개수 선정

###
(2, 4)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
(8,)
(4, 2)
```


### indexing
- list에서는 지원하지 않는 `[0, 0]`과 같은 표기법 지원

```python
a = np.array([[1, 2, 3], [4.5, 5, 6]], int)

print(a)
print(a[0, 0])  # Two dimensional array representation
print(a[0][0])

###
[[1 2 3]
 [4 5 6]]
1
1
```


### slicing
- list와 달리 행과 열을 나눠서 slicing 가능

```python
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)

print(a[:, 2:])   # 전체 row의 2열 이상
print(a[1, 1:3])  # 1 row의 1~2열
print(a[1:3])     # 1~2 row 전체

###
[[ 3  4  5]
 [ 8  9 10]]
[7 8]
[[ 6  7  8  9 10]]
```

- `start:end:step`의 구성이다 !!!

```python
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)

print(a[:, ::2])    # 전체 row의 2간격 column
print(a[::2, ::3])  # 홀수 row의 3간격 column

###
[[ 1  3  5]
 [ 6  8 10]]
[[1 4]]
```


### arrange

```python
np.arange(0, 5, 0.5).reshape(-1, 5)  # arrange(start, end, step)

###
array([[0. , 0.5, 1. , 1.5, 2. ],
       [2.5, 3. , 3.5, 4. , 4.5]])
```


### ones, zeros and empty

```python
z = np.zeros(shape=(10,), dtype=np.int8)
o = np.ones(shape=(2,5), dtype=np.int8)
e = np.empty(shape=(10,), dtype=np.int8)  # shape만 주어지고 비어있는 ndarray 생성 (memory initialization 안됨)

print(z)
print(o)
print(e)

###
[0 0 0 0 0 0 0 0 0 0]
[[1 1 1 1 1]
 [1 1 1 1 1]]
[48 31 -7  2  0  0  0  0  0  0]
```


### eye
- 대각선이 1인 행렬, k값의 index 변경 가능

```python
i = np.eye(3)
n = np.eye(N=3, M=5, dtype=np.int8)
k = np.eye(N=3, M=5, k=2, dtype=np.int8)  # k = start index

print(i)
print(n)
print(k)

###
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[[1 0 0 0 0]
 [0 1 0 0 0]
 [0 0 1 0 0]]
[[0 0 1 0 0]
 [0 0 0 1 0]
 [0 0 0 0 1]]
```


### random sampling
- 데이터 분포에 따른 sampling으로 array 생성

```python
u = np.random.uniform(0, 1, 10).reshape(2, 5)  # 균등 분포
n = np.random.normal(0, 1, 10).reshape(2, 5)   # 정규 분포

print(u)
print(n)

###
[[0.57940523 0.03172306 0.60349294 0.74975754 0.84284179]
 [0.52509685 0.01858581 0.31615604 0.23103752 0.73242413]]
[[-1.4929808  -1.49433276 -1.36045752 -0.48318193  1.06706139]
 [ 1.34819455 -0.2714097   3.14394324  0.61660097 -0.4941138 ]]
```


### sum & axis
- axis : 모든 operation function을 실행할 대, 기준이 되는 dimension 축

```python
test_array = np.arange(1, 13).reshape(3, 4)

r_sum = test_array.sum(axis=1)  # 가로(row) 방향
c_sum = test_array.sum(axis=0)  # 세로(column) 방향

print(test_array)
print(r_sum)
print(c_sum)

###
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[10 26 42]
[15 18 21 24]
```


### concatenate
- vstack : 위 아래로 합치기
- hstack : 좌우 옆으로 합치기

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))

d = np.array([[1], [2], [3]])
e = np.array([[4], [5], [6]])
f = np.hstack((d, e))

print(c)
print(f)

###
[[1 2 3]
 [4 5 6]]
[[1 4]
 [2 5]
 [3 6]]
```
- 비슷하면서도 다르다.
```python
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
c = np.concatenate((a, b), axis=0)

d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6]])
f = np.concatenate((d, e.T), axis=1)

print(c)
print(f)

###
[[1 2 3]
 [4 5 6]]
[[1 2 5]
 [3 4 6]]
```


### Element-wise operations
- shape이 같을 때 일어나는 연산

```python
matrix_a = np.arange(1, 13).reshape(3, 4)
matrix_b = matrix_a * matrix_a

print(matrix_a)
print(matrix_b)

###
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[  1   4   9  16]
 [ 25  36  49  64]
 [ 81 100 121 144]]
```


### Dot product

```python
test_a =  np.arange(1, 7).reshape(2, 3)
test_b =  np.arange(7, 13).reshape(3, 2)

test_c = test_a.dot(test_b)

print(test_a)
print(test_b)
print(test_c)

###
[[1 2 3]
 [4 5 6]]
[[ 7  8]
 [ 9 10]
 [11 12]]
[[ 58  64]
 [139 154]]
```


### broadcasting
- shape이 다른 배열 間 연산을 지원하는 기능

```python
test_matrix = np.array([[1, 2, 3], [4, 5, 6]], float)
scalar = 3

r = test_matrix + scalar

print(test_matrix)
print(scalar)
print(r)

###
[[1. 2. 3.]
 [4. 5. 6.]]
3
[[4. 5. 6.]
 [7. 8. 9.]]
```

- `4x3`과 `1x3`을 더해주면 각 row의 각 element끼리 더한다

```python
matrix_a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]], float)
matrix_b = np.array([[1, 2, 3]], float)

matrix_c = matrix_a + matrix_b

print(matrix_a)
print(matrix_b)
print(matrix_c)

###
[[ 0.  0.  0.]
 [10. 10. 10.]
 [20. 20. 20.]
 [30. 30. 30.]]
[[1. 2. 3.]]
[[ 1.  2.  3.]
 [11. 12. 13.]
 [21. 22. 23.]
 [31. 32. 33.]]
```


### all & any

```python
a = np.arange(10)

print(a)
print(a>5)          # 각 element와 비교한 결과를 array로 반환
print(np,any(a>5))  # element 중 하나라도 만족하면 True
print(np,any(a<0))  # element 중 하나도 만족하지 못하면 False
print(np,all(a>5))  # element 모두 만족하지 못하면 False
print(np,all(a<10)) # element 모두 만족하면 True

### 
[0 1 2 3 4 5 6 7 8 9]
[False False False False False False  True  True  True  True]
True
False
False
True
```


### where
- 조건에 맞는 index 반환

```python
a = np.arange(5) * 10
b = np.where(a < 30, 1, 0)
c = np.where(a > 20)

print(a)
print(b)
print(c)

###
[ 0 10 20 30 40]
[1 1 1 0 0]
(array([3, 4]),)
```


### argmin, argmax

```python
a = np.array([1, 2, 4, 5, 8, 78, 23, 3])

b = np.argmin(a)  # index 값으로 반환
c = np.argmax(a)  # index 값으로 반환

print(a)
print(b)
print(c)

###
[ 1  2  4  5  8 78 23  3]
0
5
```

```python
a = np.array([[1, 10, 4, 7], [8, 5, 78, 23], [9, 7, 6, 3]])

b = np.argmin(a, axis=0)  # column 방향
c = np.argmax(a, axis=1)  # row 방향

print(a)
print(b)
print(c)

###
[[ 1 10  4  7]
 [ 8  5 78 23]
 [ 9  7  6  3]]
[0 1 0 2]
[1 2 0]
```


### boolean index
- 특정 조건에 따른 값을 배열 형태로 추출 가능

```python
a = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
b = a[a > 5]

c = a < 3
d = a[c]

print(a)
print(b)
print(c)
print(d)

###
[1. 4. 0. 2. 3. 8. 9. 7.]
[8. 9. 7.]
[ True False  True  True False False False False]
[1. 0. 2.]
```


### fancy index
- array를 index value로 사용해서 값을 추출

```python
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)  # 반드시 integer로 선언

c = a[b]       # bracket index
d = a.take(b)  # bracket index와 같은 효과

print(a)
print(b)
print(c)
print(d)

###
[2. 4. 6. 8.]
[0 0 1 3 2 1]
[2. 2. 4. 8. 6. 4.]
[2. 2. 4. 8. 6. 4.]
```