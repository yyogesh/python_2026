# Function
#    ↓
# Function remembers something
#    ↓
# Closure : A function that remembers.
#    ↓
# Function wraps another function
#    ↓
# Decorator : A function that modifies/enhances another function.

def outer():
    def inner():
        print("Hello from inner")

    inner()

outer()

def outer():
    def inner():
        print("Hello")

    return inner


my_function = outer()

my_function()


def create_greeting(name):
    def greet():
        print("Hello", name)

    return greet


greet_yogesh = create_greeting("Yogesh")

greet_yogesh()

print(greet_yogesh.__name__)
print(greet_yogesh.__doc__)
print(greet_yogesh.__closure__[0].cell_contents)



def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
ten_times = create_multiplier(10)


def counter():

    count = 0
    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = counter()
print("*"*20)
print(counter1())
print(counter1())
print(counter1())


# def counter():
#     count = 0
#     def increment():
#        # print("Count:", count)
#         count += 1
#         return count

#     return increment

# counter1 = counter()
# print("*"*20)
# print(counter1())
# print(counter1())
# print(counter1())


# gloabl variable comes from the module/global scope.

# nonlocal variable comes from an enclosing function.

# GLOBAL
#   |
#   ↓
# outer()
#   |
#   ↓
# inner()


# global   → GLOBAL
# nonlocal → outer()
# local    → inner()

print("*"*40)
# Late Binding Gotcha

functions = []

for i in range(3):

    def show():
        print(i)

    functions.append(show)

for function in functions:
    function()

print("*"*40)

functions = []

for i in range(3):

    def show(i=i):
        print(i)

    functions.append(show)


for function in functions:
    function()


# Late binding = closure looks up the variable when the function runs.



def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count

    return increment


class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count



# @my_decorator
# def hello():
#     print("Hello")


# hello = my_decorator(hello)

# @decorator is syntax sugar for replacing a function with the decorator's result.


def my_decorator(function):

    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper

@my_decorator
def hello():
    print("Hello")


hello()


# *arg **kwarg

# functools
