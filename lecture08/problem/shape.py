import math

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        """
        Shape 클래스를 상속 받은 Circle 클래스를 정의한다.
        Shape 클래스의 shape_type 속성에는 "원" 이라는 값을 부여한다
        Circle 클래스의 radius 속성을 추가하고 param으로 받은 radius 값을 부여한다
        """

    def calculate_area(self):
        """
        원의 넓이를 return
        """

    def calculate_perimeter(self):
        """
        원의 둘레를 return
        """

class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Shape 클래스를 상속 받은 Rectangle 클래스를 정의한다.
        Shape 클래스의 shape_type 속성에는 "직사각형" 이라는 값을 부여한다
        Rectangle 클래스의 width, height 속성을 추가하고 param으로 받은 width, height 값을 부여한다
        """

    def calculate_area(self):
        """
        직사각형의 넓이를 return
        """

    def calculate_perimeter(self):
        """
        직사각형의 넓이를 return
        """

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        """
        Shape 클래스를 상속 받은 Triangle 클래스를 정의한다.
        Shape 클래스의 shape_type 속성에는 "삼각형" 이라는 값을 부여한다
        Triangle 클래스의 side1, side2, side3 속성을 추가하고 param으로 받은 side1, side2, side3 값을 부여한다
        """

    def calculate_area(self):
        """
        삼각형의 넓이를 return -> 헤론의 공식 활용
        """

    def calculate_perimeter(self):
        """
        삼각형의 둘레를 return
        """

# 도형 객체 생성 및 사용 예시
circle = Circle(5)
print(f"{circle.shape_type}의 넓이: {circle.calculate_area():.2f}")
print(f"{circle.shape_type}의 둘레: {circle.calculate_perimeter():.2f}")

rectangle = Rectangle(4, 6)
print(f"{rectangle.shape_type}의 넓이: {rectangle.calculate_area()}")
print(f"{rectangle.shape_type}의 둘레: {rectangle.calculate_perimeter()}")

triangle = Triangle(3, 4, 5)
print(f"{triangle.shape_type}의 넓이: {triangle.calculate_area()}")
print(f"{triangle.shape_type}의 둘레: {triangle.calculate_perimeter()}")
