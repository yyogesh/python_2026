# Liskov Substitution Principle (LSP)
# Subclass must behave like superclass


class Bird:

    def fly(self):
        print("Flying")


class Sparrow(Bird):
    pass


class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")


def make_bird_fly(bird):
    bird.fly()


make_bird_fly(Sparrow())
make_bird_fly(Penguin())


class Bird:
    pass

class FlyingBird(Bird):

    def fly(self):
        print("Flying")


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):

    def swim(self):
        print("Swimming")


sparrow = Sparrow()
sparrow.fly()

penguin = Penguin()
penguin.swim()


class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, w):# violates expected behavior   
        self.w = w
        self.h = w # forces height to change too - surprising!


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h


class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2


shapes = [Rectangle(4, 5), Square(3)]
for s in shapes:
    print(s.area()) 