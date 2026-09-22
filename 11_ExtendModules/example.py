from operator import itemgetter, attrgetter, methodcaller, add, sub, mul, truediv

data = {"name": "Alice", "id": 101}
name = itemgetter("name")(data)

get_id = itemgetter("id")

print(get_id(data))  # Output: 101

uppercase = methodcaller("upper")
print(uppercase("hello"))  # Output: "HELLO"

print(add(10, 20))  # Output: 30
print(sub(10, 20))  # Output: -10
print(mul(10, 20))  # Output: 200
print(truediv(10, 20))  # Output: 0.5