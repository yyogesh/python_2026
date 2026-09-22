# Global variables

count = 0  # This is a global variable

def increment():
    # global count  # This is a global variable
    count = 10 # This is a local variable
    print(f"Count: {count}")

print(f"Initial Count: {count}")  # Output: Initial Count: 0

increment()  # Output: Count: 10
increment()  # Output: Count: 10

print(f"Final Count: {count}")  # Output: Final Count: 10


def increment_global():
    global count  # This is a global variable
    count += 1
    print(f"Count: {count}")    

print(f"Initial Count: {count}")  # Output: Initial Count: 0

increment_global()  # Output: Count: 1
increment_global()  # Output: Count: 2

print(f"Final Count: {count}")  # Output: Final Count: 2


def increment_local():
    count = 0  # This is a local variable
    def inner():
        nonlocal count  # This is a nonlocal variable
        count += 1
        print(f"Count: {count}")
    inner()