# Lecture 04

## 파이썬 제어문 및 반복문 심화

### 2차원 List
#### 개념
- 2차원 List(2D List)는 List 안에 또 다른 List를 포함하는 형태로 구성된 데이터 구조이다
- 행(row)과 열(column)로 구성된 테이블 형태의 데이터를 표현할 수 있다

#### 생성
```python
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix2 = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
]
```
- `matrix1`처럼 3x4 크기의 2D List를 만들 수 있다
- `matrix2`처럼 각 row의 List 크기가 다를 수 있다

#### 접근
- `index`를 활용하여 `matrix`의 `element`에 접근할 수 있다
- 첫 번째 `index`는 행(row), 두 번재 `index`는 열(column)을 의미한다
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```
- 위처럼 `matrix`가 2D List로 정의되었을 때 아래 어떤 값들이 각각 print 될지 예상해보자
```python
print(matrix[0, 0])
print(matrix[0][0])
print(matrix[1][2])
print(matrix[3][3])
```
- 결과는 아래와 같다
```python
print(matrix[0, 0]) # Error
print(matrix[0][0]) # 1
print(matrix[1][2]) # 7
print(matrix[3][3]) # Error
```

#### 반복문을 활용한 2D List 접근
```python
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix2 = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
]

for row in matrix1:
    for element in row:
        print(element)

for row in matrix2:
    for element in row:
        print(element)
```

### 미로찾기 실습
#### 미로1
![미로1](https://github.com/chris-dev-edu/python/assets/124873454/cd25246d-a905-4d29-ba6d-d0678b3acb99)

#### 미로2
![미로2](https://github.com/chris-dev-edu/python/assets/124873454/d505b119-8b82-408e-98b5-6e7c7c9905b7)

#### 미로3
![미로3](https://github.com/chris-dev-edu/python/assets/124873454/b84d397a-8485-4803-b4e3-87d97858a0a9)

#### 미로4
![미로4](https://github.com/chris-dev-edu/python/assets/124873454/15ada8ce-7a0c-4a27-9199-373381bc010e)

### 스도쿠 실습
#### 스도쿠1
![스도쿠1](https://github.com/chris-dev-edu/python/assets/124873454/d56507cf-04e6-4755-8690-2c1e793f0add)

#### 스도쿠2
![스도쿠2](https://github.com/chris-dev-edu/python/assets/124873454/c473ff82-ab64-4f9e-85f3-7ea34d915b98)