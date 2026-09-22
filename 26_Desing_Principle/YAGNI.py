# You Aren't Gonna Need It

class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Triangle(Shape):
    pass


class ShapeExporter:
    pass


class ShapeDatabase:
    pass

#YAGNI You Aren't Gonna Need It


width = 10
height = 5

area = width * height

print("Area:", area)