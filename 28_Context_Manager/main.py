# file = open("data.txt")

# data = file.read()

# raise Exception("Something went wrong!")

# file.close()   # ❌ never executed


# with open("data.txt") as file:
#     data = file.read()


# with
#  ↓
# Open resource
#  ↓
# Use resource
#  ↓
# Exception?
#  ↓
# Cleanup
#  ↓
# Continue

# file = open("data.txt")

# try:
#     content = file.read()
# finally:
#     file.close()


# __enter__()
# __exit__()


class File:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# Create Database
#        ↓
# __enter__()
#        ↓
# return value
#        ↓
# store in db
#        ↓
# execute body
#        ↓
# __exit__()



# class Demo:
#     def __enter__(self):
#         print("ENTER")

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("EXIT")
#         print("Exception:", exc_value)


# with Demo(): # context Manager 
#     print("Inside")
#     raise ValueError("Something went wrong")





class IgnoreError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception handled")
        return True


with IgnoreError():
    raise ValueError("Oops!")

print("Program continues")




with open("input.txt") as source, open("output.txt", "w") as target:
    data = source.read()
    target.write(data)



with open("input.txt") as source:
    with open("output.txt", "w") as target:
        data = source.read()
        target.write(data)



with (
    open("input.txt") as source,
    open("output.txt", "w") as target,
    open("log.txt", "a") as log
):
    data = source.read()
    target.write(data)
    log.write("Processing completed")



from contextlib import contextmanager


@contextmanager
def demo():
    print("Before")

    yield

    print("After")


with demo():
    print("Inside")




@contextmanager
def database():
    print("Connecting")

    connection = "DB Connection"

    yield connection

    print("Closing")


with database() as db:
    print("Using:", db)