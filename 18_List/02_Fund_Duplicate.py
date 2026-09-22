numbers = [10, 20, 30, 20, 40, 10, 50, 20, 30]

duplicats = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicats:
            duplicats.append(numbers[i])

print(duplicats)

# On2

duplicats = []

print(numbers.count(20))

for item in numbers:
    if numbers.count(item) > 1 and item not in duplicats:
        duplicats.append(item)

print(duplicats)


#3
duplicats = []

seen = set()
duplicats = set()

for item in numbers:
    if item in seen:
        duplicats.add(item)
    else:
        seen.add(item)
        

print(duplicats)


#4
duplicats = []

seen = set()
duplicats = []

for item in numbers:
    if item in seen:
        if item not in duplicats:
            duplicats.append(item)
    else:
        seen.add(item)
        

print(duplicats)