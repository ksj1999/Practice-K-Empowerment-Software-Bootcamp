import math

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다')


class Circle(shape):
    def __init__(self, x, y, raidius):
        super().__init__(x, y)
        self.radius = raidius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Cyilinder(Circle):
    def __init__(self, x, y, raidius, height):
        super().__init__(x, y, raidius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height


class Rectangle(shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}입니다'

    def __add__(self, other):
        # 두 사각형 넓이의 합
        # return (self.width * self.length) + (other.width * other.length)
        # 각 사각형의 width의 합과 length의 합의 곱
        return Rectangle(0, 0, (self.width+other.width), (self.length+other.length))


cy1 = Cyilinder(20, 20, 10.0, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70, 30, 10, 15)

print(r2)
print(cy1.get_area())
print(r1)
print(r1 + r2)
print(r1.get_area())
print(c1.get_area())
print(c2.get_area())