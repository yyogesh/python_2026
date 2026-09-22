# Decorator 

def Outer(func):
    def Inner():
        print("Before calling the function")
        func()
        print("After calling the function")
    return Inner

# def display():
#     print("This is the display function.")

# r = Outer(display)
# r()

@Outer
def display():
    print("This is the display function.")

display()


