# Lecture 08

## 파이썬 클래스

### 클래스 (Class)
#### 개념
- 클래스(class)는 객체지향 프로그래밍을 구현하는데 사용된다
- 클래스는 속성(attribute)과 메소드(method)를 포함한다
- 객체지향 프로그래밍은 데이터와 그 데이터를 조작하는 메소드를 하나의 단위로 묶는 개념이다

#### 클래스 정의
```python
class 클래스명:
    def __init__(self, param1, param2, ...):
        self.attribute1 = param1
        self.attribute2 = param2
        ...

    def method1(self, param1, param2, ...):
        # 메소드 코드
        ...
    
    def method2(self, param1, param2, ...):
        # 메소드 코드
        ...
```

#### 클래스 사용
```python
객체명 = 클래스이름(param1, param2, ...)
```

#### 속성 및 메소드
```python
class MyClass:
    def __init__(self, x, y):
        self.x = x # 속성 x
        self.y = y # 속성 y

    def add(self): # 메소드 add
        return self.x + self.y

    def multiply(self): # 메소드 multiply
        return self.x * self.y

obj = MyClass(3, 4)
add_result = obj.add()
multiply_result = obj.multiply()
```

#### 상속
- 파이썬은 클래스 상속을 지원하여, 이미 존재하는 클래스의 기능을 다른 클래스에서 확장할 수 있다
- 확장된 클래스는 부모 클래스의 속성과 메소드를 사용할 수 있다

```python
class ParentClass:
    def __init__(self, name):
        self.name = name
        
    def parent_method(self):
        print("부모 클래스의 메소드")

class ChildClass(ParentClass):
    def __init__(self, name, param1, param2):
        super().__init__(name)
        self.attribute1 = param1
        self.attribute2 = param2
        
    def child_method(self):
        print("자식 클래스의 메소드")

# 객체 생성
child_obj = ChildClass()

# 상속받은 메소드 호출
child_obj.parent_method()  # 출력: "부모 클래스의 메소드"
child_obj.child_method()   # 출력: "자식 클래스의 메소드"
```

#### 다형성
- 클래스 메소드가 상황에 따라 다른 방식으로 동작할 수 있는 성질
- 동일한 메소드 이름을 가진 다른 클래스들이 각자의 방식으로 메소드를 구현할 수 있다

```python
class Dog:
    def sound(self):
        print("멍멍!")

class Cat:
    def sound(self):
        print("야옹!")

# 다형성 활용
def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)  # 출력: "멍멍!"
make_sound(cat)  # 출력: "야옹!"
```

#### Magic Method (매직 메소드)
- Magic Method는 파이썬에서 미리 정의된 특별한 이름을 가진 Method 이다
- 해당 메소드를 사용하면 클래스의 행동을 커스터마이징할 수 있다
- Magic Method는 언더스코어(`__`)로 시작하고 끝난다

1. `__init__`: 객체 생성 시 초기화를 위해 호출되는 메소드
2. `__str__`: 객체를 문자열로 표현할 때 호출되는 메소드
3. `__len__`: 객체의 길이를 반환할 때 호출되는 메소드
4. `__add__`, `__sub__`, `__mul__`, `__div__`, 등: 객체에 적용되는 연산자를 재정의할 때 호출되는 메소드