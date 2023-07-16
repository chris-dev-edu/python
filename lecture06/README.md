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

```python
num = 1

def increase_and_print_number():
    global num
    num = num + 10
    print(num)

increase_and_print_number()
```

### 모듈 (Module)

### 패키지 (Package)