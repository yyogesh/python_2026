# Returning a Function

def outer_function():
    def inner_function():
        print("This is the inner function.")

    return inner_function


my_function = outer_function()
my_function()


def outer_function(msg1):
    msg = "Hello from the outer function!"
    def inner_function():
        print(msg, msg1)

    return inner_function

my_function = outer_function("Hello, world!")
my_function()