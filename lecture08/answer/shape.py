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
        super().__init__("원")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("사각형")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("삼각형")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # 헤론의 공식을 이용하여 삼각형의 넓이 계산
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

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
