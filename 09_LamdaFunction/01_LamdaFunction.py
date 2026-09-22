def double(x):
    return x * 2

print(double(5))


double_lambda = lambda x, y: x * y * 2
print(double_lambda(5, 3))

a = lambda x, y: x + y
print(a(5, 3))

print((lambda x, y: x + y)(5, 3))


# key restriction
# no if/else, loops, or multiple statements
# no assignment, no print, no return, no import, no def, no class



l1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

f = filter(lambda x: x % 3 == 0, l1)

print(f) # <filter object at 0x000001F2A1B8C4C0>

print(list(f))



l1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

f1 = lambda x: x % 3  == 0

f = filter(f1, l1)

print(f) # <filter object at 0x000001F2A1B8C4C0>

print(list(f))


l1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def is_divisible_by_3(x):
    return x % 3 == 0

f = filter(is_divisible_by_3, l1)

print(f) # <filter object at 0x000001F2A1B8C4C0>

print(list(f))

# *****************************

l1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

f = filter(lambda x: x % 3 == 0, l1)

print(f) # <filter object at 0x000001F2A1B8C4C0>

print(list(f))

l1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

print(list(filter(lambda x: x % 3 == 0, l1)))

print(list(map(lambda x: x * 2, l1)))

print(list(map(lambda x: x if x % 2 == 0 else -x, l1)))