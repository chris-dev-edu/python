# Lecture 05

## 파이썬 함수 및 람다

### 함수(function)
#### 개념
- 함수는 작업을 수행하는 코드 블록이며, 이름을 가지고 있다
- 필요할 때마다 함수를 호출하여 코드를 실행할 수 있다
- 재사용성과 코드의 모듈화를 위해 함수를 사용한다

#### 정의와 호출
- 함수는 `def` 키워드를 사용하여 정의한다
- 함수를 호출할 때는 함수의 이름과 필요한 매개변수(parameter)를 전달한다
- 여러개의 매개변수를 갖는다면, 쉼표 `,` 로 구분한다
```python
# 함수 정의
def function_name(param1, param2, ...):
    # 함수의 동작을 구현하는 코드
    ...

# 함수 호출
function_name(param1, param2, ...)
```

#### 반환값(return)
- 함수는 실행 결과로 값을 반환할 수 있다
- `return` 키워드를 사용하여 반환할 값을 지정한다
- 반환값이 없는 경우에는 `return` 을 생략하거나 `return` 만 작성한다
```python
def function_name(param1, param2, ...):
    # 함수의 동작을 구현하는 코드
    ...
    return 반환값
```

#### 좋은 함수(Python Function Convention)
**함수명(naming)**
- 함수 이름은 소문자로 작성하고, 필요한 경우 단어 사이에 밑줄 `-`을 사용하여 가독성을 높인다
- 함수의 역할을 나타내는 명사나 동사 형태의 이름을 사용하는 것이 좋다 (ex. `calculate_sum`, `get_user_info`)

**매개변수(parameter)**
- 매개변수는 가능한 명사 형태의 이름을 사용한다
- 필수적인 매개변수는 기본적으로 작성하고, 선택적인 매개변수는 기본값을 설정한다
```python
# essential_parm = 필수 매개변수
# optional_param = 선택 매개변수
def example_function(essential_param, optional_param=1):
    # 함수의 동작을 구현하는 코드
    ...
```

#### 함수 만들기 실습
1. add_numbers(a, b) => 수 a와 b를 매개변수로 받아 합을 반환하는 함수
2. multiply_numbers(a, b) => 수 a와 b를 매개변수로 받아 곱을 반환하는 함수
3. calculate_sum(n) => 정수 n을 매개변수로 받아 1부터 n까지 정수의 합을 반환하는 함수
4. is_even(n) => 정수 n을 매개변수로 받아 짝수라면 True, 홀수라면 False를 반환하는 함수
5. calculate_circle_area(r) => 정수 r을 매개변수로 받아 반지름이 r인 원의 넓이를 구하는 함수(π = 3.141592)

#### 함수 만들기 실습 (+@)
1. 세 개의 숫자를 매개변수로 받아서 그 중 가장 작은 숫자를 반환하는 min_number() 함수를 작성하세요.
2. 두 개의 숫자를 매개변수로 받아서 그 숫자들의 합과 곱을 반환하는 sum_and_multiply() 함수를 작성하세요.
3. 정수 n을 매개변수로 받아서 1부터 n까지의 모든 숫자의 합을 반환하는 calculate_sum() 함수를 작성하세요.
4. 문자열을 매개변수로 받아서 그 문자열을 거꾸로 뒤집은 문자열을 반환하는 reverse_string() 함수를 작성하세요.
5. 정수 n을 매개변수로 받아서 n의 절대값을 반환하는 absolute_value() 함수를 작성하세요.
6. 문자열과 정수 n을 매개변수로 받아서 문자열을 n번 반복한 새로운 문자열을 반환하는 repeat_string() 함수를 작성하세요.
7. 리스트를 매개변수로 받아서 리스트의 원소들의 합을 반환하는 list_sum() 함수를 작성하세요.
8. 문자열을 매개변수로 받아서 모든 문자들을 대문자로 변환한 후 반환하는 uppercase_string() 함수를 작성하세요.
9. 정수 n을 매개변수로 받아서 n이 홀수인지 여부를 반환하는 is_odd() 함수를 작성하세요.
10. 정수 n을 매개변수로 받아서 n까지의 모든 정수를 포함하는 리스트를 반환하는 create_number_list() 함수를 작성하세요.

### 람다(lambda)
#### 개념
- 람다 표현식은 익명 함수를 간단하게 작성하기 위한 방법이다
- 람다 표현식은 일회성 함수로 사용될때 유용하다
- 람다 표현식은 `lambda` 키워드를 사용하여 정의한다
- 한 줄로 간결하게 표현할 수 있으며, 주로 함수를 인수로 받거나 반환하는 함수에서 사용된다

#### 예시
```python
add = lambda x, y: x+y

result = add(1, 2)
```

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
```

```python
names = ['Alice', 'Bob', 'Charlie', 'David']
sorted_names = sorted(names, key=lambda x: len(x))
```