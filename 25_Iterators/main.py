numbers = [1, 2, 3, 4, 5]

squares = (x * x for x in numbers)

print(squares)
print(list(squares))

numbers = [x * x for x in range(1_000_000)] # ALL STORED IN MEMORY

numbers = (x * x for x in range(1_000_000))# request → calculate → return

total = sum(x * x for x in range(1_000_000))

squares = [x * x for x in range(1_000_000)]

total = sum(squares)

# min(...)
# max(...)
# sum(...)
# any(...)
# all(...)

# result = any(
#     x > 100
#     for x in range(1_000_000)
# )

from itertools import count, cycle, repeat, groupby

numbers = count(10, 2)

print(next(numbers))
print(next(numbers))
print(next(numbers))

colors = cycle(["Red", "Green", "Blue"])

print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))


numbers = repeat(10, 5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for key, group in groupby(numbers, lambda x: x % 2):
    print(key, list(group))



data = [
    ("A", 10),
    ("A", 20),
    ("B", 30),
    ("B", 40),
    ("C", 50)
]

for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))


# A [('A', 10), ('A', 20)]
# B [('B', 30), ('B', 40)]
# C [('C', 50)]