guests = {
    "Aman",
    "Riya",
    "Aman",
    "John"
}

print(guests)

if "Aman" in guests:
    print("Allowed")

numbers = {1, 2, 3}

numbers = set([1, 2, 3, 1, 2, 3])

print(numbers)

# {}

# set()

guests.add("Sara")

guests.remove("Aman")

guests.discard("Aman")

guests.discard("Aman")


python_students = {"Aman", "Riya", "John"}

ai_students = {"Riya", "Sara", "John"}

common_students = python_students.intersection(ai_students)

all_students = python_students | ai_students

both = python_students & ai_students

only_python = python_students - ai_students

# A U B
# A & B

result = python_students ^ ai_students


a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))

B = {1, 2, 3}

A = {1, 2}

print(A.issuperset(B))

numbers = {1, 2, 3}

numbers.add(4)

numbers = frozenset([1, 2, 3])

print(numbers)


words = ["Apple", "BANANA", "apple"]

result = {
    word.lower()
    for word in words
}


numbers = [1, 2, 2, 3, 1, 4]

unique = list(set(numbers))

print(unique)

unique = list(dict.fromkeys(numbers))

print(unique)



words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }

counts = {}

for word in words:
   counts[word] = counts.get(word, 0) + 1



numbers = [1, 2, 3, 2, 4, 1]

seen = set()
duplicates = set()

for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print(duplicates)


# collection module : counter, defaultdict, deque, OrderDict