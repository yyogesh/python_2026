import json


# def main():
#     with open('data.json', 'r') as f:
#         data = json.load(f)

#     print(data)
#     print(data['name'])
#     print(data['age'])

# if __name__ == "__main__":
#     main()


student = {
    "name": "Rahul",
    "age": 25,
    "active": True
}

json_string = json.dumps(student, indent=4,  sort_keys=True)  # Convert Python object to JSON string
print(json_string)  # Convert Python object to JSON string


json_string = '''
{
    "name": "Rahul",
    "age": 25
}
'''


data = json.loads(json_string)  # Convert JSON string to Python object
print(data)


student = {
    "name": "Rahul",
    "age": 25,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(
        student,
        file,
        indent=4
    )


with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)


# dict ==> object
# list ==> array

# Python	JSON
# dict	object
# list	array
# str	string
# int	number
# float	number
# True	true
# False	false
# None	null