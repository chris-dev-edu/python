# Lecture 03

## 파이썬 제어문 및 반복문

### 제어문 if
#### if
- if 문은 조건에 따라 다른 코드 블록을 실행하는 데 사용되는 파이썬의 제어문이다
- 조건이 참(True)인 경우에만 해당 코드 블록이 실행된다
- 비교연산자를 통해 조건을 확인하고, 논리연산자를 통해 여러개의 조건을 결합한다
```python
if 1+1==2:
    print("1+1은 2입니다")
```

#### 비교연산자
| 연산자 | 설명                   |
|--------|------------------------|
| `==`   | 두 값이 같은지 비교     |
| `!=`   | 두 값이 다른지 비교     |
| `<`    | 작은지 비교            |
| `>`    | 큰지 비교              |
| `<=`   | 작거나 같은지 비교     |
| `>=`   | 크거나 같은지 비교     |

#### 논리연산자
| 연산자 | 설명                               |
|--------|------------------------------------|
| `and`  | 두 조건이 모두 참일 때 참을 반환    |
| `or`   | 두 조건 중 하나라도 참이면 참을 반환 |
| `not`  | 조건을 반대로 뒤집음               |

#### if 문 예제
- a가 b보다 크거나 같고, c 보다 작은 경우
```python
if a >= b and a < c:
    print("a가 b보다 크거나 같고, c 보다 작다")
```
- a가 b 또는 c와 같은 경우
```python
if a == b or a == c:
    print("a가 b 또는 c와 같다")
```
- a가 정수가 아닌 경우
```python
if not type(a) == int:
    print('a는 정수가 아니다')
```

#### if-elif-else 문
- 다중 조건문을 효율적으로 작성하기 위해 `if-elif-else` 구문을 사용한다
- `elif`는 `else if`의 줄임말로, 이전 조건이 거짓일 때 다음 조건을 판별한다
- score가 90점 이상인 경우 A, 80점 이상인 경우 B, 70점 이상인 경우 C, 60점 이상인 경우 D, 60점 미만인 경우 F를 출력하는 프로그램을 만들어보자
```python
score = 20
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

### 반복문 for
#### for
- for문을 활용하면 숫자범위, 리스트, 튜플, 딕셔너리, 셋, 문자열 등의 데이터 구조를 반복하여 처리할 수 있다
- 사용 방법: `for i in Sequence` (`i` 대신 다른 변수를 사용해도 된다)

#### 숫자 범위 반복
- `range(a)`: 0부터 a전 까지의 범위
- `range(a, b)`: a부터 b전 까지의 범위
- `range(a, b, c)`: a부터 b까지 c씩 증가하는 범위 (c가 음수일 수도 있음)
```python
for i in range(10):
    print(i)
```
```python
for i in range(5, 10):
    print(i)
```
```python
for i in range(20, -10, -3):
    print(i)
```

#### 리스트 반복
```python
fruits = ['apple', 'banana', 'cherry', 'melon', 'strawberry']

for fruit in fruits:
    print(fruit)
```

#### 튜플 반복
```python
numbers = (1, 3, 5, 7, 12, 1612, -12)

for number in numbers:
    print(number)
```

#### 딕셔너리 key 반복
```python
my_dict = { 'apple': 300, 'banana': 200, 'cherry': 500 }

for key in my_dict.keys():
    print(key)
```

#### 딕셔너리 value 반복
```python
my_dict = { 'apple': 300, 'banana': 200, 'cherry': 500 }

for value in my_dict.values():
    print(value)
```

#### 딕셔너리 key, value 반복
```python
my_dict = { 'apple': 300, 'banana': 200, 'cherry': 500 }

for key, value in my_dict.items():
    print(key, value)
```

#### 셋 반복
```python
my_set = {1, 3, "abcw", 1257}

for element in my_set:
    print(element)
```

#### continue와 break
- continue: 현재 반복을 중단하고, 다음 반복을 진행한다
- break: 반복문을 중단하고 빠져나온다.

```python
numbers = [1, 3, -2, -15, 67, -41, 9, 0, 22, 165, -312, 22]

for number in numbers:
    if number > 0:
        print(number)
    elif number < 0:
        continue
    else:
        break
```

### 반복문 while
- `while 조건:` 처럼 사용하여 조건이 참(True)인 동안 코드 블럭을 실행한다
- 1부터 5까지 출력하기
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
- 일치하는 패스워드를 받을 때 까지, 계속 시도하기
```python
password = ""
while password != "1234":
    password = input("비밀번호를 입력하세요: ")

print("로그인 성공")
```