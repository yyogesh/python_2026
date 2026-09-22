# Inner function is a function defined inside another function. It can access variables from the enclosing function's scope.

def outer():
    def inner():
        print("This is the inner function.")

    print("This is the outer function.")
    inner()


outer()


def totalArea(l, b, h):
    def area(length, breadth):
        return length * breadth

    def volume(length, breadth, height):
        return length * breadth * height

    print("Area of rectangle:", area(l, b))
    print("Volume of cuboid:", volume(l, b, h))


totalArea(10, 20, 30)