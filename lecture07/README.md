# Lecture 07

## 파이썬 예외 처리와 파일 입출력

### 예외 처리
#### 개념
- 예외 처리는 프로그램 실행 중에 발생하는 예외를 감지하고 처리하는 방법이다
- 예외란 프로그램 실행 도중에 예상치 못한 상황이 발생한 것을 의미하며, 이러한 상황에 대비하여 예외처리를 통해 프로그램이 비정상적으로 종료되는 것을 방지할 수 있다
- `try`, `except`, `else`, `finally` 등의 예외처리 구문을 사용하여 예외를 처리한다

#### `try`-`except` 문
- `try`: 예외가 발생할 수 있는 코드 블록을 감싸는 키워드
- `except`: `try` 블록 내에서 발생한 예외를 처리하기 위한 키워드

```python
try:
    num = int(input("정수를 입력하세요: "))
    print("입력한 정수는", num, "입니다.")
except:
    print("예외가 발생했습니다.")
```

#### `else`, `finally` 문
- `else`: `try` 블록 내에서 예외가 발생하지 않은 경우 실행되는 코드 블록
- `finally`: 예외 발생 여부와 관계 없이 항상 실행되는 코드 블록

```python
try:
    num = int(input("정수를 입력하세요: "))
    print("입력한 정수는", num, "입니다.")
except:
    print("예외가 발생했습니다.")
else:
    print("예외가 발생하지 않았습니다.")
```

```python
try:
    num = int(input("정수를 입력하세요: "))
    print("입력한 정수는", num, "입니다.")
except:
    print("예외가 발생했습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("프로그램이 종료되었습니다.")
```

#### 예외 종류
- `ValueError`: 함수의 파라미터가 값이 적절하지 않은 경우에 발생 (ex. int() 의 파라미터로 정수로 변환할 수 없는 변수를 넣은 경우)
- `TypeError`: 연산이나 함수 호출에 대한 인자의 타입이 적절하지 않은 경우에 발생
- `IndexErrror`: 리스트나 문자열 등에 인덱스 범위를 초과하여 접근하는 경우에 발생
- `SyntaxError`: 파이썬 문법 오류가 발생하는 경우에 발생
- `NameError`: 지역변수, 전역변수 이름을 찾을 수 없는 경우 발생
- `ZeroDivisionError`: 0으로 나누기가 시도되었을 때 발생
- `KeyError`: 딕셔너리에 존재하지 않는 키를 사용하려고 할 때 발생
- `FileNotFoundError`: 파일을 찾을 수 없을 때 발생
- `IOError`: 파일 입출력과 관련된 문제가 있을 때 발생
- `AttributeError`: 객체에 존재하지 않는 속성이나 메소드에 접급하려고 할 때 발생
- `ImportError`: 모듈을 가져오지 못할 때 발생

#### 특정 예외 처리하기
```python
try:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    result = num1 / num2
    print("나누기 결과:", result)
except ValueError as ve:
    print("정수를 입력해주세요.", ve)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("나눗셈이 성공적으로 수행되었습니다.")
finally:
    print("프로그램을 종료합니다.")
```

```python
try:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    result = num1 / num2
    print("나누기 결과:", result)
except (ValueError, ZeroDivisionError) as err:
    print("정수를 입력해주세요.", err)
else:
    print("나눗셈이 성공적으로 수행되었습니다.")
finally:
    print("프로그램을 종료합니다.")
```


### 파일 입출력
#### 개념
- 파일 입출력은 파이썬에서 파일에 데이터를 쓰거나 파일로부터 데이터를 읽는 작업이다
- `open` 함수를 사용하여 파일을 열고, `read`, `write`, `close` 등의 메소드로 파일을 다룬다
- 파일을 열 때는 파일의 경로와 이름을 지정하고, 읽기모드(`r`), 쓰기모드(`w`) 등을 선택한다
- 파일을 다룬 후에는 반드시 `close` 메소드를 호출하여 파일을 닫아야 한다

#### 파일 읽기
```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
        file.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
```

#### 파일 쓰기
```python
try:
    with open('output.txt', 'w') as file:
        file.write("파일 입출력 예시입니다.")
        print("파일 쓰기가 완료되었습니다.")
        file.close()
except IOError:
    print("파일을 쓸 수 없습니다.")
```