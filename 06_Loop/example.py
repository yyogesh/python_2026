numbers = [4,8,15,16,23,42,7]

target = 16

for n in numbers:

    if n == target:
        print("Found",target)
        break

    print("Checking",n)



numbers = [1,-2,3,-4,5,-6,7]

for n in numbers:

    if n < 0:
        continue

    print("Positive:",n)



lines = ["Hello","","World"," ","Python"]

for line in lines:
    if not line.strip():
        continue
    print(line)


# pass statement
for i in range(5):
    pass


# class MyClass:
#     pass

options = ["Option 1", "Option 2", "Option 3"] 
# Enumerate the options and print their index and value

for enum, option in enumerate(options):
    print(f"Index: {enum}, Option: {option}")


# zip function
list1 = [1, 2, 3]
list2 = [4, 5, 6]
zipped = zip(list1, list2)
print(list(zipped))

for name, score in zip(["Alice", "Bob", "Charlie"], [85, 90, 95]):
    print(f"{name}: {score}")

zipped = zip(list1, list2)
print(list(zipped))


zipped = zip(list1, list2)
print(dict(zipped))


print([x**2 for x in range(10)])


names = ["Alice", "Bob", "Cara"]
scores = [90, 85, 92]


for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i}: {name} - {score}")


print([name.upper() for name in ["alice", "bob", "cara"]])

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print([num for row in matrix for num in row])

# nested for loop 

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

total = 0

for row in matrix:
    for num in row:
        total += num

print("Total:", total)

rows = 5

for i in range(1, rows + 1):
    print("*" * i)