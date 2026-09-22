d = {'name':'Alice', 'age':25, 'city':'Delhi'}

print(hash('hello')) #-7906020488434913716 #DOS attack
print(hash('world')) #1234567890123456789 #DOS attack

# But int/float/tuple hashes are STABLE across runs
print(hash(42))         # always 42
print(hash(3.14))       # always same #322818021289917443
print(hash((1,2,3)))    # always same #529344067295497451

#list mutable order index, all duplicate value
# tuple immutable order index, all duplicate value
# set mutable unordered index, no duplicate value
# dict mutable unordered key, no duplicate value


student = {
    "name": "Yogesh",
    "age": 25
}

print(student["name"])
print(student["age"])

print(student.get("name"))
print(student.get("age1", "Not Found")) # Not Found


student = {
    "name": "Yogesh"
}

student["age"] = 25

print(student)

student = {
    "name": "Yogesh",
    "age": 25
}

student["age"] = "asdf"

print(student)

del student["age"]

print(student)

student.pop("name")

print(student)


student = {
    "name": "Yogesh",
    "age": 25
}

print(student.keys(), student.values(), student.items())

for key, value in student.items():
    print(key, ":", value)


if "name" in student:
    print("Key exists")
else:
    print("Key does not exist")


data = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(len(data))


numbers = {
    "a": 10,
    "b": 20,
    "c": 30
}

total = 0

for value in numbers.values():
    total += value

print(total)

print(sum(numbers.values()))

print(max(numbers.values()))

print(min(numbers.values()))

print(sorted(numbers.values()))

print(sorted(numbers.values(), reverse=True))

print(max(numbers, key=numbers.get))


keys = ["name", "age", "city"]

values = ["Yogesh", 25, "Gurgaon"]

student = dict(zip(keys, values))

print(student)

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

swapped = {}

for key, value in data.items():
    swapped[value] = key

print(swapped)

print({value: key for key, value in data.items()})


dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4,
    "a": 5
}

dict1.update(dict2)

print(dict1)

print(dict1 | dict2) # Python 3.9+ only

result = {**dict1, **dict2} # Python 3.5+ only
print(result)


numbers = {
    "a": 1,
    "b": 2,
    "c": 3
}

squares = {
    key: value**2 
    for key, value in numbers.items()
}

print(squares)


text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)




text = "python is easy and python is powerful"

words = text.split() # list of words

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)



text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

most_common = max(frequency, key=frequency.get)

print(most_common)





numbers = [1, 2, 3, 2, 4, 1, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

duplicates = []

for key, value in frequency.items():
    if value > 1:
        duplicates.append(key)

print(duplicates)

