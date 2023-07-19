# Lecture 06

## 파이썬 스코프, 모듈, 패키지

### 스코프 (Scope)
#### 개념
- Scope는 변수와 함수의 유효성과 접근성을 결정하는 규칙을 의미한다
- 변수와 함수가 정의되고 참조될 수 있는 위치를 지정하며, 해당 위치에서만 해당 변수와 함수에 접근할 수 있다

#### 종류
- 전역 범위(Global Scope)
  - 전역 범위는 모든 함수 및 클래스 외부에서 정의된 변수와 함수들이 속하는 범위이다
  - 전역 범위에서 정의된 변수와 함수는 모든 코드에서 접근할 수 있다
  - 전역 변수는 프로그램이 시작될 때 생성되며, 프로그램이 종료될 때까지 유지된다
- 지역 범위(Local Scope)
  - 지역 범위는 함수 내부에서 정의된 변수와 함수들이 속하는 범위이다
  - 지역 범위에서 정의된 변수와 함수는 해당 함수 내부에서만 접근할 수 있다
  - 함수가 호출될 때마다 새로운 지역 범위가 생성되며, 함수가 종료되면 해당 범위가 사라진다

#### 예제
```python
num = 10 # 전역 변수

def create_number():
    num = 20 # 지역 변수
    return num

print(num)
```
- `num = 10`은 전역 변수에 해당한다
- `create_number`함수 내의 `num=20`은 지역 변수에 해당한다

```python
num = 1 # 전역 변수

def print_number():
    print(num) # 전역 변수 num을 불러옴

print_number()
```

```python
num = 1

def increase_and_print_number():
    num = num + 10
    print(num)

increase_and_print_number()
```
- 에러 발생: 전역변수 `num`을 불러올 수는 있지만, 변수에 새로운 값을 할당 할때는 지역변수를 찾으려고 하기 때문이다

```python
num = 1

def increase_and_print_number():
    global num
    num = num + 10
    print(num)

increase_and_print_number()
```
- `global` 키워드를 활용하면, 함수 내에서 전역 변수에 새로운 값을 할당 할 수 있다

### 모듈 (Module)
#### 개념
- 모듈은 파이썬 코드를 구성하는 독립적인 기능 단위로 사용되는 파일이다
- 모듈은 함수, 변수, 클래스 그리고 실행 가능한 코드를 포함 할 수 있다
- 모듈은 `.py` 확장자를 가진 단일 파일로 구성된다

#### 사용법
```python
import MODULE_NAME1
# or
import MODULE_NAME2 as CUSTOM_NAME

MODULE_NAME1.FUNCTION_NAME1()
CUSTOM_NAME.FUNCTION_NAME2()
```

#### 표준 모듈과 사용자 생성 모듈
`표준 모듈`
- `math`, `datetime`, `time` 등
- https://docs.python.org/ko/3/library/index.html

`사용자 생성 모듈`
- 사용자가 생성한 `.py` 확장자 파일 모듈

### 패키지 (Package)
- 관련된 모듈들을 디렉토리로 구성한 것이다

**예시**
```python
import urllib.request

response = urllib.request.urlopen("https://www.example.com")
html = response.read()
print(html)
```
- urllib 패키지 내에 존재하는 request 모듈을 가져다 사용하는 예제