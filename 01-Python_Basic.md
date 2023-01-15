# 01주차 파이썬 기초


## Agenda

1. 파이썬/AI 개발환경 준비하기
2. 파이썬 기초 문법 I
3. 파이썬 기초 문법 II


## Summary

- 파이썬에 대한 어원부터 정말 친절하게 잘 정리된 강의였지만, 1.5배속으로 들었다.
- miniconda 설치를 이용한 JupyterNotebook 환경 구축도 가이드 해주지만, colab이 편할 것 같다.
- 그동안 햇갈렸던 것 몇 가지 내용들을 잘 알 수 있게 되었다! 개꿀!!!
- 우와 만만하게 봤는데, 1.5배속으로 해도 많다. 그리고, 정말 Python 기초 내용 다 설명해준다! 우와!
- Coding Style
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  - [Google Python Style Guide (번역)](https://github.com/Yosseulsin-JOB/Google-Python-Style-Guide-kor)
  - [VSCODE - Google Python Style Guide 적용](https://technote.kr/383)
  - [VSCODE - black으로 code format 자동화하기](https://lovedh.tistory.com/entry/vscode에서-black으로-code-format-자동화하기-python)
  - [VSCODE - flake8 설치(PEP8 검사)](https://blog.naver.com/dsz08082/222281152333)
- 뒷부분은 공부해야할 것이 좀 있다.
- 길다.
- 해당 강의는 아래 링크의 수업이 출처인 듯 하다.
  - https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC


## 기억하면 좋을 것

### call by reference
```python
a = [5, 4, 3, 2, 1]
b = a

a.sort()
print(b)

# b는 a와 같은 주소를 바라보기에 같은 결과가 나온다
```

### packing / unpacking
```python
t = [1, 2, 3]

a, b, c = t

# 갯수가 맞아야 한다
```

### parameter vs argument
- parameter: 함수의 입력 값 인터페이스
- argument: 실제 parameter에 대입된 값

### f-string
Python 3.6 이후, PEP498에 근거한 formatting 기법
```python
name = 'whatwant'
age = 48

print(f"Hello, {name}. You are {age}.")
print(f'{name:20}')    # 패딩 20칸
print(f'{name:>20}')   # 오른쪽 정렬 + 패딩 20칸
print(f'{name:*<20}')  # 왼쪽 정렬 + 패딩 20칸 + 빈칸에 * 채우기
print(f'{name:*>20}')  # 오른쪽 정렬 + 패딩 20칸 + 빈칸에 * 채우기
print(f'{name:*^20}')  # 가운데 정렬 + 패딩 20칸 + 빈칸에 * 채우기

number = 3.141592653589793
print(f'{number:.2f}') # 소숫점 2째자리
```

### all(), any()
```python
boolean_list = [True, False, True, False, True]

all_value = all(boolean_list)  # 모두 True?
any_value = any(boolean_list)  # 하나라도 True?

print(f'all : {all_value}')
print(f'any : {any_value}')
```

### raw string
```python
print(r'글씨를 쓰다가 \n 이걸 써도 줄이 안바뀐다')
```

### function type hints
Python 3.5 이후, PEP484에 기반하여 type hints 기능 제공
```python
def type_hint_example(name: str) -> str
  return f'Hellp, {name}'
```

### docstring
VSCode에서 **Python Docstring Generator** extention 설치 후, Ctrl+Shift+p, **Generate Docstring** 실행하면 됨
```python
def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum

print(add_binary.__doc__)
```

### list vs tuple
tuple은 값 변경 불가
```python
l = [1, 2, 3]
t = (1, 2, 3)

t1 = (1)  # 정수로 인식
t2 = (1,) # 값이 하나인 tuple은 반드시 ","를 붙여야 함
```

### set
값을 순서 없이 저장, 중복 불허하는 자료형
```python
s = set([3, 1, 2, 2, 3])   # s = {3, 1, 2, 2, 3}
print(s)                   # {1, 2, 3}

s.add(1)
print(s)                   # {1, 2, 3}

s.remove(1)
print(s)                   # {2, 3}

s.update([1, 4, 5, 6, 7])
print(s)                   # {1, 2, 3, 4, 5, 6, 7}

s.discard(3)
print(s)                   # {1, 2, 4, 5, 6, 7}

s.clear()
print(s)                   # set()


s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

s = s1.union(s2)
print(s)                # {1, 2, 3, 4, 5, 6, 7}

s = s1 | s2
print(s)                # {1, 2, 3, 4, 5, 6, 7}

s = s1.intersection(s2)
print(s)                # {3, 4, 5}

s = s1 & s2
print(s)                # {3, 4, 5}

s = s1.difference(s2)
print(s)                # {1, 2}

s = s1 - s2
print(s)                # {1, 2}
```


### OrderedDict
Python 3.6 이후, 기존 Dict에서도 입력한 순서를 보장하여 출력하기에 필요 없어짐


### list comprehension
```python
result = []
for i in range(10):
  result.append(i)

print(result)

result = [i for i in range(10)]

print(result)
```

### zip
```python
math = (100, 90, 80)
kor = (90, 90, 70)
eng = (90, 80, 70)

value = zip*math, kor, eng)

print(value)
```

### lambda function
함수 이름 없이, 함수처럼 사용할 수 있는 익명 함수. 수학의 람다 대수에서 유래
```python
f = lambda x, y : x + y

print(f(1,4))
```

### map
list의 각 요소에 특정 동작을 적용
'''python
ex = [1, 2, 3, 4, 5]

f = lambda x, y : x + y

print( list( map(f, ex, ex)))
```

### iterable object
미리 메모리에 올리는 것이 아니라 사용될 때 올라오게 되는 방식
- 내부적 구현으로 __iter__와 __next__가 사용됨
- iter()와 next()함수로 iterable 객체를 iterator object로 사용
```python
cities = ['Seoul', 'Busan', 'Jeju']

iter_obj = iter(cities)

print(iter_obj)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(iter_obj)          # Error
```

### generator
- iterable object를 특수한 형태로 사용해주는 함수
- element가 사용되는 시점에 값을 메모리에 반환
  - yield를 사용해 한 번에 하나의 element만 반환함
```python
def general_list(value):
  result = []
  for i in range(value):
    result.append(i)
  return result

def generator_list(value):
  result = []
  for i in range(value):
    yield i
```

### generator comprehension (= generator expression)
- list comprehension과 유사한 형태로 generator 형태의 list 생성
- [] 대신 () 사용
```python
gen_ex = (n*n for n in range(500))

print(type(gen_ex))
```

### keyword arguments
```python
def print_something(my_name, your_name):
  print(f'Hello {your_name}, My name is {my_name}')

print_something('whatwant', 'sally')                    # Hello sally, My name is whatwant
print_something(your_name='sally', my_name='whatwant')  # Hello sally, My name is whatwant
```

### default arguments
```python
def print_something(my_name, your_name='sally'):
  print(f'Hello {your_name}, My name is {my_name}')

print_something('whatwant')              # Hello sally, My name is whatwant
print_something('whatwant', 'chani')     # Hello chani, My name is whatwant
```

### variable-length parameter
개수가 정해지지 않은 변수를 함수의 parameter로 사용하는 방법
```python
def asterisk_test(a, b, *args):
  return a+b+sum(args)

print(asterisk_test(1, 2, 3, 4, 5))    # 15


def asterisk_test(*args):
  x, y, z = args
  return x, y, z

print(asterisk_test(1, 2, 3))   # (1, 2, 3)
```

### keyword variable-length parameter
```python
def kwargs_test_1(**kwargs):
  print(kwargs)                             # {'first': 1, 'second': 2, 'third': 3}

kwargs_test_1(first=1, second=2, third=3)


def kwargs_test_2(one, two=3, * args, **kwargs):
  print(one+two+sum(args))                   # 13
  print(args)                                # ()
  print(kwargs)                              # {'first': 3, 'second': 4, 'third': 5}

kwargs_test_2(one=10, first=3, second=4, third=5)
```
