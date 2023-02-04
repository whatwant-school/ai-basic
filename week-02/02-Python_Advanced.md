# 02주차 파이썬 다지기


## Agenda

4. 파이썬 기초 문법 III
5. 파이썬으로 데이터 다루기


## Python OOP

- 젠장... Python OOP 강의 메모한 것 날려먹었음 ㅠㅠ


## Module and Project

### module

- `02_fah_convert.py` 파일은, `import 02_fah_convert` 에러 ← 숫자로 시작하는 파일명 금지
  - [예제 - 02_module_ex1.py](02_module_ex1.py)
- 특정 디렉토리 밑에 모듈 파일이 있을 경우에는 `from ~ import ~` 방식으로 불러오면 된다
  - 해당 디렉토리에는 `__init__.py` 파일이 있는 것을 권장 (Python 3.3+ 없어도 무방)
  - [예제 - 02_module_ex2.py](02_module_ex2.py)
- 절대/상대 경로 모듈 참조
```python
from game.graphic.render import render_test  # 절대 경로
from .render import render_test              # 현재 디렉토리 기준
from ..sound.echo import echo_test           # 부모 디렉토리 기준
```


### namespace

- Alias
```python
import fah_converter as fah

print(fah.convert_c_to_f(41.6))
```
- 모듈에서 특정 함수 또는 클래스만 호출
```python
from fah_converter import convert_c_to_f

print(convert_c_to_f(41.6))
```
- 모듈에서 모든 함수 또는 클래스 호출
```python
from fah_converter import *

print(convert_c_to_f(41.6))
```


## Exception/File/Log Handling

### Exception Handling
- [예제 - 02_exception.py](02_exception.py)
- 파일 오픈 에러와 같은 경우에는 `if else` 보다는 `try except` 구분을 권장
- 필요에 따라 강제로 Exception 발생 : raise
```python
while True:
    values = input("변환할 정수 값을 입력해주세요")
    for digit in values:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않으셨습니다")
    print(f"정수값으로 변환된 숫자 - {int(value)}")
```


### File Handling
- File Read
```python
f = open("i_have_a_dream.txt", "r")
contents = f.read()
print(contents)
f.close()

with open("i_have_a_dream.txt", "r") as my_file
    contents = my_file.read()
    print(contents)
```
- File Write
```python
f = open("count_log.txt", "w", encoding="utf8")
for i range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

with open("count_log.txt", "a", encoding="utf8") as my_file
    for i range(1, 11):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)
```

### Log Handling
- 기본 log 관리 모듈
- [예제 - 02_log.py](02_log.py)
```python
import logging

logging.debug("틀렸잖아!")
logging.info("확인해")
logging.warning("조심해!")
logging.error("에러났어!!!")
logging.critical("망했다!!!")
```
- logging formmater
```python
formatter = logging.Formatter("%(asctime)s %(levelname)s %(process)d %(message)s")

2018-01-18 22:47:04,385 ERROR 4410 ERROR occurred
2018-01-18 22:47:04,458 INFO 4439 HERE WE ARE
```
- logging config를 파일로 관리할 수도 있음
  - [예제 - 02_csv_write.py](02_csv_write.py)
  - [예제 - 02_logging.cfg](02_logging.cfg)


### configparser
- [예제 - 02_configparser.py](02_configparser.py)
- key값은 무조건 소문자로 불러옴


### argparser
- [예제 - 02_argparser.py](02_argparser.py)
- `dest` 명칭의 변수이름으로 매칭


## Data Handling

### CSV (Comma/Character Separate Values)
- CSV 파일 읽고 쓰는 예제
  - [예제 - 02_csv_read.py](02_csv_read.py)
  - [예제 - 02_csv_write.py](02_csv_write.py)
- `,`가 데이터 중간에 있을 경우 전처리 필요 → CSV 객체 활용하면 해결됨
  - 중간에 `,`가 있더라도 전체를 하나의 아이템으로 묶어주기 위한 `quotechar`
```python
import csv

reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
```
- `CP949` 인코딩된 CSV 파일을 `UTF8`로 변환하는 예제
  - [예제 - 02_csv_object.py](02_csv_object.py)


### WWW (World Wide Web)


### 정규식/Regex (Regular Expression)
- 정규식 연습장 : https://regexr.com/
```regex
010-0000-0000     ^\d{3}\-\d{4}\-\d{4}$
IPv4              ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$
                  ([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})
이메일            ^[a-zA-Z0-9]+@[a-zA-Z0-9]+$
                  ^[_0-9a-zA-Z]+@[0-9a-zA-Z]+(.[_0-9a-zA-Z-]+)*$
휴대폰            ^01(?:0|1|[6-9])-(?:\d{3}|\d{4})-\d{4}$
일반전화          ^\d{2,3}-\d{3,4}-\d{4}$
주민등록번호      \d{6} \- [1-4]\d{6}
```
- 메타 문자
  - `.` : `\n`을 제외한 모든 문자와 매치
  - `*` : 앞에 있는 글자를 반복해서 나올 수 있음
  - `+` : 앞에 있는 글자를 최소 1회 이상 반복
  - `?` : 반복 횟수 1회
  - `|` : or
  - `^` : not
- `http`로 시작해서`zip`으로 끝나는 문자열 찾기
```regex
/(http)(.+)(zip)/g
```


### 정규식 검색 (findall)
- [예제 - 02_regex_findall.py](02_regex_findall.py)
- [예제 - 02_regex_findall_stock.py](02_regex_findall_stock.py)


### BeautifulSoup install with venv
- BeautifulSoup 사용을 위해서는 패키지 설치가 필요
- 깔끔한 관리를 위해 Python 가상환경 사용
```bash
# 가상환경 설치
$ python -m venv .venv

# 가상환경 활성화
$ source .venv/Scripts/activate

# bs4 (BeautifulSoup 4) 설치
$ pip install bs4
$ pip install lxml

# 현재 설치된 패키지 정보 저장
$ pip freeze > requirements.txt

# 패키지 설치
$ pip install -r requirements.txt

# 가상환경 종료
$ deactive
```


### XML (eXtensible Markup Language)
- [예제 - 02_xml_books.py](02_xml_books.py)
- [예제 - 02_xml_patent1.py](02_xml_patent1.py)
- [예제 - 02_xml_patent2.py](02_xml_patent2.py)


### JSON (JavaScript Object Notation)
- [예제 - 02_json_read.py](02_json_read.py)
- [예제 - 02_json_write.py](02_json_write.py)


