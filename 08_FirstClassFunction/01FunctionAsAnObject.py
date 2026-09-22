# function as an object

print(print.__doc__)

print(print.__name__)

show = print

show("Hello")

def greet(name):
    return f"Hello {name}"

say_hello = greet

print(say_hello("Arjun"))