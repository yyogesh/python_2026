print(hash("apple"))


data = {
    "name": "Aman",
    10: "number",
    (1, 2): "tuple"
}

# wrong
# data = {
#     [1, 2]: "list"
# }

# Mutable object → generally not hashable
# Immutable object → often hashable

#__hash__  __eq__


data = {
    "name": "Aman",
    10: "number",
    (1, 2): "tuple"
}

print(data["name"])
print(data[10])
print(data[(1, 2)])


data = {
    "name": "Aman",
    10: "number",
    (1, 2): "tuple"
}

print(data.get("name"))
print(data.get("name1", "Not Found"))

student = {
    "name": "Riya"
}

student["age"] = 20


count = {}

name = "Aman"

count.setdefault(name, 0)

count["Aman"] += 1


counts = {}

words = ["apple", "banana", "apple"]

for word in words:
    counts[word] = counts.get(word, 0) + 1


for word in words:
    counts.setdefault(word, 0)
    counts[word] += 1



a = {
    "name": "Aman",
    "age": 20
}

b = {
    "city": "Delhi",
    "age": 21
}

a.update(b)

print(a)


a = {"name": "Aman"}
b = {"age": 20}

c = a | b



a = {"name": "Aman"}
b = {"age": 20}

c = {**a, **b}


student = {
    "name": "Riya",
    "age": 20
}

age = student.pop("age")


data = {
    "a": 1,
    "b": 2,
    "c": 3
}

item = data.popitem()


student = {
    "name": "Riya",
    "age": 20
}

student.keys()

student.values()

print(student.items())

for key, value in student.items():
    print(key, value)


students = {
    "s1": {
        "name": "Aman",
        "age": 20
    },
    "s2": {
        "name": "Riya",
        "age": 21
    }
}

print(students["s1"]["name"])
print(students["s2"]["age"])

city = data["user"]["address"]["city"]

#?.

city = data.get("user", {}).get("address", {}).get("city")

numbers = [1, 2, 3]

square = [x* x for x in numbers]

squares = {
    x: x * x for x in range(1, 6)
}


data = {
    "Aman": 1,
    "Riya": 2
}

inverted = {
    value: key
    for key, value in data.items()
}


names = [
    ("India", "Aman"),
    ("India", "Riya"),
    ("USA", "John")
]

# {
#     "India": ["Aman", "Riya"],
#     "USA": ["John"]
# }

from collections import defaultdict, OrderedDict

groups = defaultdict(list) # empty list

for country, name in names:
    groups[country].append(name)

print(groups)


data = {}

data["first"] = 1
data["second"] = 2
data["third"] = 3


