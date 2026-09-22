class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student(name={self.name!r}, marks={self.marks})"

    def __str__(self):
        return f"{self.name} scored {self.marks} marks"

student = Student("Rahul", 90)
student1 = Student("Rahul", 90)

print(repr(student))  # Student(name='Rahul', marks=90)

print(student.__str__())  # Student(name='Rahul', marks=90)

print(student.__eq__(student1))  # True

# a  + b


class Student1:
    def __repr__(self):
        return "Student('Rahul')"

    def __str__(self):
        return "Str Student('Rahul')"

student2 = Student1()

print(student2)



class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, spec):
        if spec == "usd":
            return f"${self.amount:.2f}"

        if spec == "inr":
            return f"₹{self.amount:.2f}"

        return str(self.amount)


money = Money(1000)
print(f"Money: {money}")  # Money: 1000
print(f"Money: {money:usd}")  # Money: $1000.00
print(f"Money: {money:inr}")  # Money: ₹1000.00

print(bytes(12))

# money.__bytes__()


class Message:
    def __init__(self, text):
        self.text = text

    def __bytes__(self):
        return self.text.encode("utf-8")

message = Message("Hello, World!")
print(bytes(message))  # b'Hello, World!'


print(dir(message))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'text']

print(hash("123abc"))


class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def __eq__(self, other):
        return self.roll_no == other.roll_no

    def __hash__(self):
        return hash(self.roll_no)


s1 = Student(1)
s2 = Student(2)

print(s1 == s2)

print(hash(s1))  # Output: Hash value based on roll_no


# __eq__      ==
# __ne__      !=
# __lt__      <
# __le__      <=
# __gt__      >
# __ge__      >=

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0

cart = ShoppingCart([])
print(bool(cart))

if cart:
    print("Cart has items")
else:
    print("Cart is empty")


class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


# print(len())

# __add__
# __sub__
# __mul__
# __truediv__
# __floordiv__
# __mod__
# __pow__
# __neg__
# __pos__
# __abs__
# __round__


# __int__
# __float__
# __complex__
# __index__


# __len__
# __getitem__
# __setitem__
# __delitem__
# __contains__
# __iter__
# __next__
# __reversed__


class Team:
    def __init__(self, players):
        self.players = players

    def __getitem__(self, index):
        return self.players[index]


team = Team(["Rahul", "Amit", "Priya"])
print(team[0])

