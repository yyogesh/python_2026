import pickle

student = {
    "name": "Rahul",
    "marks": [80, 90, 85]
}

with open('student.pkl', 'wb') as f:
    pickle.dump(student, f)


with open('student.pkl', 'rb') as f:
    loaded_student = pickle.load(f)

print(loaded_student)



import shelve as sh

with sh.open('student.shelve') as f:
    f['name'] = 'Rahul'
    f['marks'] = [80, 90, 85]

with sh.open('student.shelve') as f:
    print(f['name'])
    print(f['marks'])



with sh.open("students") as db:
    db["student1"] = {
        "name": "Rahul",
        "age": 25
    }


import struct

with open('data.bin', 'wb') as f:
    f.write(b"Hello")

with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)