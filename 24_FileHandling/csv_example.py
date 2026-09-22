# id,name,amount
# 1,Rahul,500
# 2,Amit,750
# 3,Neha,900

import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow([1, 'Rahul', 25])
    writer.writerow([2, 'Amit', 30])
    writer.writerow([3, 'Neha', 28])


with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['amount'])


students = [
    ["id", "name", "age"],
    [1, "Rahul", 25],
    [2, "Amit", 26]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)


fields = ["id", "name", "age"]

students = [
    {"id": 1, "name": "Rahul", "age": 25},
    {"id": 2, "name": "Amit", "age": 26}
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)