# Lecture 01

## 파이썬 변수와 자료구조 (1)

### 변수
- python에서는 변수를 사용하여 값을 저장할 수 있다
- 변수를 선언할 때 자료형을 지정할 수도 있고, 지정하지 않아도 된다
  - 자료형을 지정하지 않는 경우 
    ```python
    name = "John"
    age = 25
    pi = 3.14
    is_student = True
    ```
    
  - 자료형을 지정하는 경우
    ```python
    name: str = "John"
    age: int = 25
    pi: float = 3.14
    is_student: bool = True
    ```

### 변수명
- 변수명에는 알파벳(대소문자), 숫자, 밑줄, 유니코드문자를 사용할 수 있다
```python
# 아래 처럼 변수명을 지을 수 있다.
Number = 33
lucky_number = 7
_nums = 777
num_안녕 = 175
내_숫자 = 1273
```

- 숫자는 변수명의 첫 글자가 될 수 없다
```python
number1 = 365 # OK
3number = 333 # Error
```

- 파이썬에서 특정 의미를 가지는 예약어는 변수명으로 사용할 수 없다
  - ex. `if`, `for`, `while`, `print` 등...
- 변수명을 지을 때는 다음과 같은 규칙을 따르는 것이 일반적이다
  - 소문자와 밑줄 사용
  - 변수의 용도와 이름을 잘 설명할 수 있는 변수명 정하기
  - 상수 변수는 대문자로 작성
    ```python
    small_circle_radius = 7
    big_circle_radius = 37
    PI = 3.141592
    small_circle_area = small_circle_radius * small_circle_radius * PI
    big_circle_area = big_circle_radius * big_circle_radius * PI
    ```

### 자료형
- 파이썬은 변수의 자료형을 미리 선언할 필요가 없다(그러나 선언해 주어도 된다)
- 주요 자료형: 정수(int), 실수(float), 문자열(str), 불리언(bool) 
```python
var_int = 3
var_float = 3.14
var_str = 'Hello'
var_bool = True
```
- `type()`을 활용하여 자료형을 확인할 수 있다
```python
print(type(var_int))
print(type(var_float))
print(type(var_str))
print(type(var_bool))
```

### List(리스트)
- List는 대괄호`[]`로 표현되며, 여러개의 값을 순서대로 저장할 수 있다
- 리스트 안의 여러 값들을 element(요소)라고 한다
- List에서 index(인덱스)를 사용하여 특정 위치의 값을 가져올 수 있다
  - index는 0부터 시작하고, 음수 index는 뒤에서 부터 역순으로 접근
- List의 일부분을 추출하기 위해 slicing(슬라이싱)을 사용할 수 있다
  ```python
  sub_list1 = my_list[1:3] # index 1부터 2까지의 값 추출
  sub_list2 = my_list[3:7] # index 3부터 6까지의 값 추출
  
  # 아래는 어떻게 slicing이 되는지 시도해보기
  sub_list3 = my_list[1:-1]
  sub_list4 = my_list[-4:-1]
  sub_list5 = my_list[-1:-4]
  ``` 
- List 요소 추가: `my_list.append(6)`
- List 요소 삭제: `my_list.remove(3)` - 3이라는 값을 가진 element 삭제
- List 길이 확인: `length = len(my_list)`
- List 정렬: `my_list.sort()`
- List 검색: `index = my_list.index(4)` - 4라는 값을 가진 element의 index 검색

### Tuple(튜플)
- Tuple은 소괄호`()`로 표현되며, List와는 다르게 변경 불가능한 자료형이다
- Tuple도 List와 마찬가지로 index로 특정위치의 값을 가져올 수 있다.

### 연산자
#### 산술연산자
| 연산자 | 설명                     |
|--------|--------------------------|
| `+`    | 덧셈                     |
| `-`    | 뺄셈                     |
| `*`    | 곱셈                     |
| `/`    | 나눗셈 후, 실수 결과 반환 |
| `//`   | 나눗셈 후, 정수 결과 반환 (몫) |
| `%`    | 나눗셈 후, 나머지 반환   |
| `**`   | 거듭제곱                 |

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

#### 할당연산자
| 연산자 | 설명                                       |
|--------|--------------------------------------------|
| `=`    | 변수에 값을 할당                            |
| `+=`   | 변수에 값을 더하고 결과를 변수에 할당       |
| `-=`   | 변수에서 값을 빼고 결과를 변수에 할당       |
| `*=`   | 변수에 값을 곱하고 결과를 변수에 할당       |
| `/=`   | 변수를 값으로 나누고 결과를 변수에 할당     |
| `//=`  | 변수를 값으로 나눈 몫을 변수에 할당        |
| `%=`   | 변수를 값으로 나눈 나머지를 변수에 할당    |
| `**=`  | 변수를 값으로 거듭제곱하고 결과를 변수에 할당 |
