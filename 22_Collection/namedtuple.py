student = ("Amit", 25, 90)


print(student[0])
print(student[1])
print(student[2])

from collections import namedtuple

student = namedtuple("student", ["name", "age", "marks"])

student = student("Amit", 25, 90)

print(student)
print(student.name)
print(student.age)
print(student.marks)



from collections import namedtuple

Student = namedtuple("Student", "name age marks")

students = [
    Student("Amit", 20, 90),
    Student("Rahul", 21, 85),
    Student("Priya", 20, 95)
]

for student in students:
    print(student.name, student.marks)



from collections import OrderedDict

data = OrderedDict()

data["A"] = 1
data["B"] = 2
data["C"] = 3

print(data)
data.move_to_end("A")
print(data)


# functools LRU_cache


#                     collections
#                          │
#           ┌──────────────┼──────────────┐
#           │              │              │
#        Counter       defaultdict       deque
#           │              │              │
#           ▼              ▼              ▼
#       Frequency        Grouping       Queue/Stack
#           │              │              │
#           ▼              ▼              ▼
#       Anagrams       Graph          Sliding Window
#       Top K          Index          BFS
#       Duplicates     Grouping       Rotation
#       First unique   Graph          Palindrome

#     ├── Sliding Window
#     ├── Two Pointers
#     ├── Frequency Map
#     ├── Prefix Sum
#     ├── LRU Cache
#     └── Memoization



# typing



def add(a, b):
    return a + b


def add(a: int, b: int) -> int:
    return a + b


# items: list