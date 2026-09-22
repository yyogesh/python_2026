from functools import cache, lru_cache, wraps
import time


def logger(function):
    def wrapper():
        print("Function started")

        function()

        print("Function finished")

    return wrapper


@logger
def say_hello():
    print("Hello Python!")


say_hello()


# angular 

# @injectable()
# export class SomeClass {
#   constructor() {}
# }

# logging 
# timer
# authentication

#                 ┌── logging
# Function ───────┼── timing
#                 ├── retry(3)
#                 └── validation


# react hoc // ...props


def my_decorator(function):

    def wrapper(*args, **kwargs):
        print("Before")
        result = function(*args, **kwargs)
        print("After")
        return result

    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

print("*" * 50)


def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@my_decorator
def calculate():
    """Calculate something."""
    pass


print(calculate.__name__)



from functools import wraps


def repeat(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator

@repeat(times=3)
def hello():
    print("Hello")

hello()

# retry(times=3)
#        ↓
#    decorator
#        ↓
#     wrapper
#        ↓
#  process()



def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        elapsed = (end - start) * 1000

        print(f"{function.__name__}: {elapsed:.2f} ms")

        return result

    return wrapper


@timer
def calculate():
    total = sum(range(1_000_000))
    return total


calculate()


@cache
def square(number):
    print("Calculating...")
    return number * number


print(square(10))
print(square(10))
print(square(10))



@lru_cache(maxsize=128)
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# @rate_limit(calls=10, period=1)
# def call_api():
#     pass


def validate_age(function):

    @wraps(function)
    def wrapper(age):

        if age < 18:
            raise ValueError("Age must be 18 or above")

        return function(age)

    return wrapper


@validate_age
def register_user(age):
    print("User registered")



def deprecated(message):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            print(
                f"WARNING: {function.__name__} "
                f"is deprecated. {message}"
            )
            return function(*args, **kwargs)
        return wrapper

    return decorator

@deprecated("Use calculate_total() instead.")
def calculate():
    return 100



# @app.route("/users")
# def users():

# @app.get("/users")
# def users():

# @pytest.mark.parametrize(...)
# def test_add():