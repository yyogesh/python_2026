from typing import ClassVar, Final, List, Optional, Union, Any, Callable, NoReturn
from __future__ import annotations


def add(a, b):
    return a + b


def add(a: int, b: int) -> int:
    return a + b


name: str = "Aman"
age: int = 25
salary: float = 150000.0
is_active: bool = True


def log_message(message: str) -> None:
    print(message)


def fail(message: str) -> NoReturn:
    raise RuntimeError(message)


# -> None
#     Function finishes and returns None

# -> NoReturn
#     Function never reaches a normal return


class Employee:
    def get_manager(self) -> Employee:
        pass

# Without postponed evaluation, older Python 
# versions had situations where the class name wasn't available yet.
# future annotations = "Don't evaluate my type hints immediately."


def total(*args: int) -> int:
    return sum(args)

print(total(10, 20, 30))

def create_user(**kwargs: str) -> None:
    print(kwargs)


numbers: List[int] = [10, 20, 30]

prices: dict[str, float] = {
    "Milk": 60.0,
    "Bread": 40.0
}

user: tuple[int, str] = (101, "Yogesh")

numbers: tuple[int, ...] = (10, 20, 30, 40)


name: Optional[str] = None

name: str | None = None


def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Yogesh"

    return None


data: Any = "Hello"

data = 100
data = [1, 2, 3]
data = {"name": "Yogesh"}


# operation: Callable[[int, int], int]

def add(a: int, b: int) -> int:
    return a + b

operation: Callable[[int, int], int] = add

print(operation(10, 20))


MAX_RETRIES: Final[int] = 3


class Employee:
    company: ClassVar[str] = "ABC Technologies"

    name: str



# dict[str, int]

from typing import TypeAlias

UserScores: TypeAlias = dict[str, int]


scores: UserScores = {
    "Yogesh": 95,
    "Rahul": 88
}

from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]


numbers = first([10, 20, 30])

names = first(["Yogesh", "Rahul"])


from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


numbers = Stack[int]()

numbers.push(10)
numbers.push(20)
numbers.push(30)

print(numbers.pop())
print(numbers.pop())
print(numbers.pop())

names = Stack[str]()

names.push("Yogesh")
names.push("Rahul")


user = {
    "id": 101,
    "name": "Yogesh",
    "active": True
}


from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    active: bool


user: User = {
    "id": 101,
    "name": "Yogesh",
    "active": True
}


from typing import Literal

method: Literal["GET", "POST"]

method = "GET"
method = "POST"




from typing import overload

@overload
def get_value(value: int) -> int:
    ...

@overload
def get_value(value: str) -> str:
    ...

def get_value(value: int | str) -> int | str:
    return value




from typing import Self

class Builder:

    def set_name(self, name: str) -> Self:
        self.name = name
        return self



# mypy.ini

# [mypy]
# python_version = 3.12
# strict = true


#pyproject.toml

# [tool.mypy]
# python_version = "3.12"
# strict = true

value = legacy_function()  # type: ignore

value = legacy_function()  # type: ignore[assignment]