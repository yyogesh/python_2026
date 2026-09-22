from ctypes.macholib import framework


fruits = ["apple", "banana", "cherry"]

for abc in fruits:
    print(abc)


for i in range(2, 10):
    print(i)


count = 1

while count <= 5:
    print(count)
    count += 1



for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


for i in range(10):
    if i % 2 == 0:
        break
    print(i)


colors = ["red", "green", "blue"]

for c in enumerate(colors):
    print(f"Index: {c[0]}, Color: {c[1]}")

for i, c in enumerate(colors):
    print(f"Index: {i}, Color: {c}")


# python collections


list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
dictionary = {"a": 1, "b": 2, "c": 3}

for i in list:
    print(i)

for i in tuple:
    print(i)

for i in set:
    print(i)

for i in dictionary:
    print(i, dictionary[i])


password = "python123"

attempt = 0

while attempt < 3:
    entered = input("Enter password: ") #123

    if entered == password:
        print("Access granted")
        break
    attempt += 1
else:
    print("Access denied")



numbers = [10,20,30,40]

target = 50

for n in numbers:

    if n == target:
        print("Found")
        break
else:
    print("Not found")



n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
