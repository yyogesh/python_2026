l1 = [2, 8, 3, 4, 5, 7, 8, 9, 10]

print(list(filter(lambda x: x % 3 == 0, l1)))

print(list(map(lambda x: x * 2, l1)))

print(list(map(lambda x: x if x % 2 == 0 else -x, l1)))

print(sorted(l1))

print(sorted(['apple', 'date', 'cherry', 'banana']))

print(sorted(['apple', 'date', 'cherry', 'banana'], key=len))

l2 = [[4, 2, 'Six'], [1, 4, 'Five'], [2, 2, 'Four']]

print(sorted(l2))

print(sorted(l2, key = lambda x: x[0] + x[1]))


# iterator or generator expression

l1 = [3, 4, 5, 7, 8, 9, 10]

# for x in l1:
#     print(x)

it = iter(l1)

print(next(it))
print(next(it))


for x in range(4):
    print(x)


# generator expression

print("Generator expression")
def myRange(n):
    i  = 0
    while i < n:
        yield i
        i += 1

m = myRange(4)

print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

# for x in myRange(4):
#     print(x)


# any and all ==> every and some 


# import turtle

# t = turtle.Turtle()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# turtle.done