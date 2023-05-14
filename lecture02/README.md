# Lecture 02

## 파이썬 변수와 자료구조 (2)

### Dictionary(딕셔너리)
- Dictionary는 key(키)와 value(값)의 쌍으로 이루어진 자료구조다
- 중괄호`{}`를 사용하여 생성하며, 각각의 key와 value는 콜론`:`으로 구분된다
- Dictionary는 순서가 없고, 각 key는 유일해야 합니다.

#### Dictionary 생성 및 접근
```python
# 빈 Dictionary 생성
my_dict = {}

# key-value 쌍을 포함한 Dictionary 생성
# apple, banana, orange는 key가 되고 3, 5, 2가 value가 된다
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# my_dict의 apple키의 값을 출력한다: 3
print(my_dict['apple'])
```

#### key-value 쌍 추가 및 삭제
```python
# key-value 쌍 추가
my_dict['grape'] = 7

# key-value 쌍 삭제
del my_dict['banana']
```

#### 공통 메소드
```python
# Dictionary 길이 확인(key-value 쌍의 수)
length = len(my_dict)

# Dictionary의 모든 key 확인
keys = my_dict.keys()

# Dictionary의 모든 value 확인
values = my_dict.values()

# Dictionary의 모든 key-value 쌍 확인
items = my_dict.items()

# Dictionary 순회
for key, value in my_dict.items():
    print(key, value)
```

### Set(셋)
- Set은 중복되지 않은 항목들로 이루어진 자료구조이다
- 중괄호`{}`를 사용하여 생성하며, 각 항목은 콤마`,`로 구분된다
- Set은 순서가 없고, 중복된 데이터를 넣어도 한번만 들어간다

#### Set 생성 및 접근
```python
# 빈 Set 생성
my_set = set()

# 값을 포함한 Set 생성
my_set = {1, 2, 3, 4, 5}

# Set 값에 접근(순서가 없으므로 index로 접근 불가)
for item in my_set:
    print(item)
```

#### element 추가 및 삭제
```python
# element 추가
my_set.add(6)

# element 삭제
my_set.remove(3)
```

#### 공통 작업 및 메소드
```python
# Set 길이 확인
length = len(my_set)

# Set에 특정 element가 포함되어 있는지 확인
contains = 3 in my_set

# Set의 집합 계산
A = {1, 2, 3}
B = {3, 4, 5}

intersection = A.intersection(B)
union = A.union(B)
differenceA_B = A.difference(B)
differenceB_A = B.difference(A)

print("A ∩ B", intersection)
print("A ∪ B", union)
print("A - B", differenceA_B)
print("B - A", differenceB_A)
```