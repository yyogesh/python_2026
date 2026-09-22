# Function as a parameter
def Welcome():
    print("Welcome to the world of Python!")


def greet(func):
    print("Hello!")
    func() # calling the function passed as a parameter
    print("Goodbye!")

greet(Welcome)


def Welcome_French():
    print("Bienvenue dans le monde de Python!")

greet(Welcome_French)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(func, a, b):
    print(func(a, b)) # calling the function passed as a parameter

calculate(add, 4, 3)
calculate(subtract, 4, 3)   