# 4주차 - 기초 튼튼, 수학 튼튼

# 데이터 시각화 (Visualization)

- https://github.com/TEAMLAB-Lecture/AI-python-connect/tree/master/codes/ch_2/5


## matplotlib

- pyplot 객체를 사용하여 데이터를 표시


### 단점

- argument를 kwargs 받음
  - 고정된 argument가 없어서 alt + tab으로 확인이 어려움 (tip 확인이 어려움)

- Graph는 원래 figure 객체에 생성됨
  - pyplot 객체 사용시, 기본 figure에 그래프가 그려짐 → 겹쳐서 표현됨

```python
import matplotlib.pyplot as plt
import numpy as np 

X_1 = range(100)
Y_1 = [np.cos(value) for value in X]

X_2 = range(100)
Y_2 = [np.sin(value) for value in X]

plt.plot(X_1, Y_1)
plt.plot(X_2, Y_2)
plt.plot(range(100), range(100))

# 3개 graph가 하나의 화면에 같이 출력됨
plt.show()    # show & flush


# figure로 처리하면 분리하여 출력할 수 있음
fig = plt.figure() # figure 반환
fig.set_size_inches(10,10)
ax_1 = fig.add_subplot(1,2,1)
ax_2 = fig.add_subplot(1,2,2)

ax_1.plot(X_1, Y_1, c="b")
ax_2.plot(X_2, Y_2, c="g")

# 2개의 graph가 나란히 분리되어 출력
plt.show()
```