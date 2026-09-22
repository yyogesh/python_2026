empty = ()

t1 = (1, 2, 3)

print(t1)

t2 = 'a', 'b','c' # packing

print(t2)

print(tuple([10, 20, 30]))

print(tuple("hello") )

t = (10, 20, 30, 40, 50)

print(t[0])
print(t[-1])
print(t[1:4])

# t = (10, 20, 30, 40, 50)

# t[0] = 100

a = (1, 2)
b = (3, 4)
print(a + b) 
print(a * 3) 

t = (5, 10, 15)
print(10 in t) 

for x in t:
    print(x)    

# example of packing and unpacking
t = (1, 2, 3)
a, b, c = t

print(a, b, c)

t = (1, 2, 3, 4)
a, b, *c = t

print(a, b, c)

t = (1, 2, 2, 3, 2)
print(t.count(2))

print((1, 2) < (1, 3)) 
print((1, 2, 3) == (1, 2, 3))

t2 = 'a', 'b','c' # packing
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))



squares = tuple(x**2 for x in range(1, 6))
print(squares)


#(x, y) point


def add(a, b): return a + b
def sub(a, b): return a - b

operations = (add, sub)
result1 = operations[0](10, 5)
result2 = operations[1](10, 5)
print(result1, result2)




names = ("Alice", "Bob")
scores = (95, 87)
# print(zip(names, scores))
for name, score in zip(names, scores):
    print(f"{name}: {score}")



from typing import NamedTuple

#__slot__ is used to save memory and improve performance by preventing the creation of a dynamic __dict__ for each instance of the class. Instead, it allows the class to have a fixed set of attributes, which can lead to more efficient memory usage and faster attribute access.

class Point(NamedTuple):
    x: int
    y: int


p1 = Point(3, 4)
print(p1.x, p1.y)


# Set 
# Dictionary