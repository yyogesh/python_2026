# Python  DSA 
#  ML ==> MATH 
# AI ===> data process  

def create_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


create_profile("Riya", 24, "Delhi") # positional arguments

create_profile(age=30, name="Amit", city="Mumbai") # keyword arguments

create_profile("Riya", city="Mumbai", age=30) # mixed arguments


def total(a, b, *numbers):
    print(f"Calculating total for: ${a}, ${b}, ${numbers}")
    return sum(numbers)

print(total(1, 2, 3, 4, 5))  # Output: 15
print(total(10, 20, 30))  # Output: 60
print(total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: 55

# *args is used to pass a variable number of arguments to a function
# *args will create tuple of arguments passed to the function

# def total(*numbers, a, b, ):
#     print(f"Calculating total for: ${a}, ${b}, ${numbers}")
#     return sum(numbers)

# print(total(1, 2, 3, 4, 5)) 

def display_info(**details):
    print(f'Received: {details}')  # always a dict
    

display_info(name='Alice', age=25, city='Delhi')


def mixed_args(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_args(1, 2, 3, 4, 5, name='Alice', age=25)


packed = 1, 2, 3
print(packed)  # Output: (1, 2, 3)
print(type(packed))


a, b, c = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


x, y, z = [10, 20, 30]
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30


first, *rest = [1, 2, 3, 4, 5]
print(first)  # Output: 1
print(rest)  # Output: [2, 3, 4, 5]


first, *middle, last = [1, 2, 3, 4, 5]
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5



# first, *middle, last = [1]
# print(first)  # Output: 1
# print(middle)  # Output: []
# print(last)  # Output: None

*head, tail = "hello"
print(head)  # Output: ['h', 'e', 'l', 'l']
print(tail)  # Output: 'o'



first, *_, last = [1, 2, 3, 4, 5]
print(first)  # Output: 1
#print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5


def greet(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

greet("Alice", 25, "New York")  # Positional arguments
greet(age=30, name="Bob", city="Los Angeles")  # Keyword arguments

info = ("Charlie", 35, "Chicago")
greet(*info)  # Unpacking a tuple into positional arguments


def mixed_args(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_args(1, 2, 3, 4, 5, name='Alice', age=25)

info_dict = {"city": "London", "age": 25, "name": "Bob"}
greet(**info_dict)


def connect(host, port, timeout=30, use_ssl=True):
    print(f"Connecting to {host}:{port} with timeout={timeout} and use_ssl={use_ssl}")


connect("example.com", 80)  # Using default values for timeout and use_ssl
connect("example.com", 443, timeout=10)  # Overriding timeout
connect("example.com", 443, timeout=10, use_ssl=False)  # Overriding both timeout and use_ssl

#Scope of variables in Python
# LEGB Rule
# Local, Enclosing, Global, Built-in

x = 10

def show_x():
    print(f"Inside function, x = {x}")

show_x()

def change_x():
    x = 20
    print(f"Inside function, x = {x}")

change_x()

print(f"Outside function, x = {x}")


def change_global():
    global x
    x = 30
    print(f"Inside function, x = {x}")

change_global()

print(f"Outside function, x = {x}")


def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x  # Refers to the enclosing variable
        x += 5
        print(f"Inside inner_function, x = {x}")

    inner_function()
    print(f"Inside outer_function, x = {x}")

outer_function()


