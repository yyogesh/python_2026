from dataclasses import InitVar, dataclass, field

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )



@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def discount(self, percentage):
        self.price -= self.price * percentage / 100

product1 = Product("Laptop", 1000.0, 5)
print(product1)  # Output: Product(name='Laptop', price=1000.0, quantity=5)


@dataclass
class User:
    name: str
    age: int
    roles: list[str] = field(default_factory=list) # []


user1 = User("John Doe", 30)
user2 = User("Jane Doe", 25, roles=["admin"])

user2.roles.append("user")
print(user1)  # Output: User(name='John Doe', age=30, roles=[])
print(user2)  # Output: User(name='Jane Doe', age=25, roles=['admin', 'user'])


@dataclass
class User:
    username: str
    password: str = field(repr=False)


user = User("johndoe", "secretpassword")
print(user)  # Output: User(username='johndoe', password=***)


@dataclass
class User:
    id: int
    name: str
    last_login: str = field(compare=False)



@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(10, 20)
# point.x = 30  # This will raise an error because the dataclass is frozen


# __init__()

# __post_init__()


@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")


product = Product("Laptop", 100)


# Product(...)
#      ↓
# generated __init__()
#      ↓
# attributes assigned
#      ↓
# __post_init__()
#      ↓
# validation / extra initialization

#InitVar  

@dataclass()
class User:
    username: str
    password: InitVar[str]

    def __post_init__(self, password):
        print("Received password", password)

user = User("admin", "secret")

# slot 

# __get__()
# __set__()
# __delete__()

class PositiveNumber:

    def __get__(self, obj, owner):
        return obj._value

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Value must be positive")

        obj._value = value

    def __delete__(self, obj):
        del obj._value


class MyClass:
    value = PositiveNumber()


obj = MyClass()
obj.value = 10


class Product:
    def set_price(self, value):
        if value <= 0:
            raise ValueError()

    def set_quantity(self, value):
        if value <= 0:
            raise ValueError()