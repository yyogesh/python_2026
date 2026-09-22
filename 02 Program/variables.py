import sys


x = 123

print(type(x))  # Output: <class 'int'>
print(id(x))

x = 3.14

print(type(x))  # Output: <class 'float'>
print(id(x))

x = "Hello"

print(type(x))  # Output: <class 'str'>
print(id(x))


a = 10
b = a
print(a)  # Output: 10
print(b)  # Output: 10
print(id(a))  # Output: (some memory address)
print(id(b))  # Output: (same memory address as a)


p = "Hello"
q = p
print(p)  # Output: Hello
print(q)  # Output: Hello
print(id(p))  # Output: (some memory address)
print(id(q))  # Output: (same memory address as p)

q = "World"
print(p)  # Output: Hello
print(q)  # Output: World
print(id(p))  # Output: (same memory address as before)
print(id(q))  # Output: (new memory address)


a = 100
b = 100
print (a == b)  # Output: True
print (a is b)  # Output: True (small integers are cached by Python)
print(id(a) == id(b))  # Output: True (same memory address as before)

s1 = "Hello"
s2 = "Hello"
print (s1 is s2)  # Output: True

s3 = "Hello World"
s4 = "Hello World"
print (s3 is s4, "Value is")  # Output: False 

# is checks for identity (whether two variables point to the same object in memory),
# # while == checks for equality (whether the values of the objects are the same).

# print(100 == 100)  # Output: True
# print(100 is 100)  # Output: True (small integers are cached by Python)

name = "Alice"

age2 = 25

_private_variable = "This is a private variable"

camelCaseVariable = "This is a camelCase variable"

snake_case_variable = "This is a snake_case variable"

CONSTANT_VARIABLE = "This is a constant variable"

# 2Name
#my-name
# class
# my name

x, y , z = 0, 1, 2
print(x, y, z)  # Output: 0 1 2

print(isinstance(42, (int, float)))  # Output: True

print(type(42))  # Output: <class 'int'>

# id, type, isinstance, dir, help, len, print, input, range, etc. are built-in functions in Python that provide various functionalities for working with objects and data.


print(sys.getsizeof(42))  # Output: (size of the integer object in bytes)

print(sys.getsizeof(82))

print(sys.getsizeof(1))


