class File:
    def read(self):
        return "file data"


class Database:
    def read(self):
        return "database data"


def read_data(file_obj):
    print(file_obj.read())


f = File()
d = Database()

read_data(f)
read_data(d)


1 + 2 # 3

"Hello " + "World" # "Hello World"

[1, 2] + [3, 4] # [1, 2, 3, 4]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2



class User:

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


u1 = User(1)
u2 = User(2)

print(u1 == u2)