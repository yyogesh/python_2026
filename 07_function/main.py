# Rag 
# MCP client server 

score1, name1 = 87, "Arjun"
grade1 = "A" if score1 >= 90 else "B" if score1 >= 75 else "C" if score1 >= 60 else "F"
print(f"{name1}: {grade1}")

score2, name2 = 92, "Priya"
grade2 = "A" if score2 >= 90 else "B" if score2 >= 75 else "C" if score2 >= 60 else "F"
print(f"{name2}: {grade2}")

students = [
    ("Arjun", 87),
    ("Priya", 92),
    ("Rohan", 54)
]

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


for name, score in students:
    grade = get_grade(score)
    print(f"{name}: {grade}")



def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Arjun"))
print(greet("Priya", "Hi"))


def min_max(numbers):
    return min(numbers), max(numbers)


# {}


numbers = [3, 1, 4, 1, 5, 9]
minimum, maximum = min_max(numbers)
print(f"Minimum: {minimum}, Maximum: {maximum}")


def say_hello(name):
    print(f"Hello, {name}!")

#None

def find_first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n

    return None


numbers = [3, 1, 4, 1, 5, 9]
first_negative = find_first_negative(numbers)
print(f"First negative number: {first_negative}")


def create_profile(name, age, city):
    return f"{name}, {age}, from {city}"


print(create_profile("Riya", 24, "Delhi"))


print(create_profile(age=30, name="Amit", city="Mumbai"))

print(create_profile("Riya", city="Mumbai", age=30))



def create_profile(name, age, city="New York"):
    return f"{name}, {age}, from {city}"



def send_email(to, subject, body, cc=None, priority="normal"):
     print(f"To: {to}")
     print(f"Subject: {subject}")

     if cc:
        print(f"CC: {cc}")
     print(f"Priority: {priority}")


send_email(
    "boss@co.com",
    "Report",
    "Please find attached"
    "manager@co.com",
    priority="urgent"
)

cart = []

def add_item(item, cart):
    cart.append(item)
    return cart



print(add_item("apple", cart))

print(add_item("banana", cart))


def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
