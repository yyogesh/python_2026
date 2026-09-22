
a = {
    "name": "Aman"
}

b = a.copy()

b["name"] = "Riya"

print(a)
print(b)


a = {
    "user": {
        "name": "Aman"
    }
}

b = a.copy()

b["user"]["name"] = "Riya"

print(a)
print(b)

import copy

a = {
    "user": {
        "name": "Aman"
    }
}

b = copy.deepcopy(a)

b["user"]["name"] = "Riya"

print(a)
print(b)

