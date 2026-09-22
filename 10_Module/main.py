data = [0, "", None, [], 5]

print(any(data)) # some
print(all(data)) # every

numbers = [10, 20, 30]

print(any(x > 25 for x in numbers))

print(all(x > 25 for x in numbers))

password = "password123"

checkes = [
    len(password) >= 8,
    any(c.isupper() for c in password),
    any(c.islower() for c in password),
    any(c.isdigit() for c in password)
]

print(all(checkes))