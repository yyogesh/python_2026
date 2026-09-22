#                   Employee
#                     │
#           ┌─────────┴─────────┐
#           │                   │
#        Developer            Manager
#           │
#        SeniorDev


class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is coding")

class Manager(Employee):
    def work(self):
        print("Manager is managing")

class SeniorDev(Developer):
    def work(self):
        print("Senior Developer is coding and mentoring")



class Animal:

    def eat(self):
        print("Eating")
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def bark(self):
        print("Barking")

    # def sound(self):
    #     print("Woof")

    #  def sound(self):
    #         super().sound()
    #         print("Woof")


dog = Dog()
dog.eat()  # Inherited method from Animal class
dog.bark()
dog.sound()  # Calls the overridden sound method from Dog class




class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


print(D().show())  # Output: D B C A

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# MRO (Method Resolution Order) is the order in which Python looks for a method in a hierarchy of classes. 
# In the case of multiple inheritance, Python uses the C3 linearization algorithm to determine the order in 
# which classes are searched for methods. The MRO can be viewed using the `mro()` method or the `__mro__` attribute of a class.


#        A       B
#         \     /
#           C


class Printer:
    def print_document(self):
        print("Printing")


class Scanner:
    def scan_document(self):
        print("Scanning")


class AllInOne(Printer, Scanner):
    pass


    #     A
    #    / \
    #   B   C
    #    \ /
    #     D

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


e = Employee("Raj", 50000)
print(e.name)  # Output: Raj
print(e.salary)  # Output: 50000



class A:

    def __init__(self):
        print("A")


class B(A):

    def __init__(self):
        print("B")
        super().__init__()


class C(A):

    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):

    def __init__(self):
        print("D")
        super().__init__()



# Abstract class or method

from abc import ABC, abstractmethod


class Shape(ABC):

    def describe(self):
        print("I am a shape")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(10, 5)

print(r.area())
print(r.perimeter())
print(r.describe())