# Gang of Four (GoF) patterns are divided into three major categories.

# Design Patterns
# │
# ├── Creational
# │   └── How objects are created
# │
# ├── Structural
# │   └── How objects/classes are composed
# │
# └── Behavioural
#     └── How objects communicate and behave


# Creational
# │
# ├── Singleton
# ├── Factory Method
# ├── Abstract Factory
# ├── Builder
# ├── Prototype
# └── Registry


# Application Configuration
# Logger
# Database Connection Pool
# Cache


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)



# module.py

config = {
    "environment": "development"
}


# config.py

environment = "development"

database_url = "localhost"


# import config

# print(config.environment)


# Let another function/class decide which object to create.

def create_notification(notification_type):
    if notification_type == "email":
        return EmailNotification()

    if notification_type == "sms":
        return SmsNotification()

    raise ValueError("Unknown notification type")


notification = create_notification("email")

notification.send("Hello")


# Abstract Factory: Create a family of related objects.

# Windows UI
#     Button
#     Checkbox
#     TextBox

# Mac UI
#     Button
#     Checkbox
#     TextBox


class WindowsUIFactory:

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


factory = WindowsUIFactory()

button = factory.create_button()
checkbox = factory.create_checkbox()



# Builder


user = User(
    name="Yogesh",
    email="...",
    phone="...",
    address="...",
    preferences={},
    roles=[],
)

import copy
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    active: bool = True

    def __post_init__(self):
        self.email = self.email.lower()




# python
# project => 1st oct 2026
# fastAPI => 1st NOV 2026 


# Prototype

class Document:
    def __init__(self, content, metadata):
        self.content = content
        self.metadata = metadata  # Mutable object

    def __str__(self):
        return f"Doc: {self.content}, Meta: {self.metadata}"



original = Document("Hello", {"author": "Alice"})

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original) 



#Registry

class PluginRegistry:
    plugins = {}

    @classmethod
    def register(cls, name, plugin):
        cls.plugins[name] = plugin

    @classmethod
    def get(cls, name):
        return cls.plugins[name]


PluginRegistry.register("logger", LoggerPlugin())
PluginRegistry.register("database", DatabasePlugin())

logger = PluginRegistry.get("logger")
database = PluginRegistry.get("database")


# Structural
# │
# ├── Adapter
# ├── Decorator
# ├── Proxy
# ├── Composite
# ├── Facade
# └── Flyweight


class PaymentService:

    def pay(self, amount):
        pass


class StripeClient:

    def make_payment(self, value):
        pass

class StripeAdapter(PaymentService):

    def __init__(self, stripe_client):
        self.stripe_client = stripe_client

    def pay(self, amount):
        self.stripe_client.make_payment(amount)


stripe_client = StripeClient()
adapter = StripeAdapter(stripe_client)
adapter.pay(100)


# Decorator

def log_call(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print("Finished")

        return result

    return wrapper


@log_call
def calculate(a, b):
    return a + b


# Proxy : A class that controls access to another class
# Put another object in front of the real object.

class RealDatabase:
    def query(self, q):
        return f"Results for {q}"

class DatabaseProxy:
    def __init__(self):
        self._real_db = RealDatabase()
        self._cache = {}
        
    def __getattr__(self, name):
        # Control access logic
        if name == "query":
            def cached_query(q):
                if q not in self._cache:
                    self._cache[q] = self._real_db.query(q)
                return self._cache[q]
            return cached_query
        return getattr(self._real_db, name)

db = DatabaseProxy()
print(db.query("SELECT * FROM users"))


# Composite: A tree structure of objects that can be treated as a single object

# File
# Folder
#     ├── File
#     ├── File
#     └── Folder
#           ├── File
#           └── File


class File:
    def __init__(self, name): self.name = name
    def show(self): print(f"File: {self.name}")

class Folder:
    def __init__(self, name): 
        self.name = name
        self.children = []
    def add(self, item): self.children.append(item)
    def show(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show()


root = Folder("Root")
root.add(File("a.txt"))
sub = Folder("Sub")
sub.add(File("b.txt"))
root.add(sub)
root.show()

# Facade: A wrapper class that provides a simplified interface to a complex subsystem.



class CPU:
    def freeze(self): return "CPU Frozen"
class Memory:
    def load(self): return "Memory Loaded"
class HardDrive:
    def read(self): return "HDD Read"

class ComputerFacade:
    """Facade providing a simple 'start' method."""
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HardDrive()
        
    def start(self):
        return f"{self.cpu.freeze()} -> {self.memory.load()} -> {self.hdd.read()}"

pc = ComputerFacade()
print(pc.start())



# Flyweight

class FlyweightFactory:
    _flyweights = {}
    
    @classmethod
    def get_flyweight(cls, key):
        if key not in cls._flyweights:
            cls._flyweights[key] = f"SharedObject-{key}"
        return cls._flyweights[key]


a = FlyweightFactory.get_flyweight("A")
b = FlyweightFactory.get_flyweight("A")

# sum(10000000)


# Behavioural Patterns


# Behavioural
# │
# ├── Observer
# ├── Strategy
# ├── Command
# ├── Iterator
# ├── Template Method
# ├── State
# └── Chain of Responsibility


class EventEmitter:
    def __init__(self):
        self._events = {}
        
    def on(self, event, callback):
        self._events.setdefault(event, []).append(callback)
        
    def emit(self, event, *args):
        for cb in self._events.get(event, []):
            cb(*args)


emitter = EventEmitter()
emitter.on("greet", lambda name: print(f"Hello {name}"))
emitter.emit("greet", "Alice")


# Strategy Pattern: Strategy can simply be passing a callable.


def pay_by_card(amount):
    print(f"Card payment: {amount}")


def pay_by_upi(amount):
    print(f"UPI payment: {amount}")


def checkout(amount, payment_strategy):
    payment_strategy(amount)

checkout(1000, pay_by_card)


# Command Pattern : Command pattern is a behavioral design pattern that 
# converts a request or a series of requests into an object, thus decoupling the client from the concrete classes.

class SaveCommand:

    def execute(self):
        service.save()



class AddCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
        
    def execute(self):
        self.receiver.append(self.value)
        
    def undo(self):
        self.receiver.pop()


data = []
cmd = AddCommand(data, 42)
cmd.execute()
print(data) # [42]
cmd.undo()
print(data) # []


# Iterator Pattern

class Counter:

    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.maximum:
            raise StopIteration

        self.current += 1

        return self.current


for number in Counter(5):
    print(number)



# Template Method: A fixed sequence of operations while allowing specific steps to vary.

# process()
#  ├── validate()
#  ├── execute()
#  └── notify()


from abc import ABC, abstractmethod

class DataMiner(ABC):
    def mine(self):
        """Concrete skeleton"""
        self.extract()
        self.parse()
        
    @abstractmethod
    def extract(self): pass
    
    @abstractmethod
    def parse(self): pass

class CSVDataMiner(DataMiner):
    def extract(self): print("Extracting CSV")
    def parse(self): print("Parsing CSV")


miner = CSVDataMiner()
miner.mine()


# State Pattern: Object behaviour changes depending on its current state


class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


class ConcreteStateA:
    def handle(self, context):
        print("ConcreteStateA handles request")
        context.state = ConcreteStateB()

class ConcreteStateB:
    def handle(self, context):
        print("ConcreteStateB handles request")
        context.state = ConcreteStateA()


context = Context(ConcreteStateA())
context.request()
context.request()

# dict of state -> handler or class per state.
class TrafficLight:
    def __init__(self):
        self.state = "Green"
        
    def change(self):
        states = {"Green": "Yellow", "Yellow": "Red", "Red": "Green"}
        self.state = states[self.state]
        print(f"Light is now {self.state}")


light = TrafficLight()
light.change() # Yellow
light.change() # Red


# Chain of Responsibility

# Request
#    ↓
# Authentication
#    ↓
# Authorization
#    ↓
# Validation
#    ↓
# Rate Limit
#    ↓
# Business Logic

class Handler:
    def __init__(self):
        self.next_handler = None
        
    def set_next(self, handler):
        self.next_handler = handler
        return handler
        
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return "Not Handled"

class AuthHandler(Handler):
    def handle(self, request):
        if request == "auth":
            return "Authenticated"
        return super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        if request == "log":
            return "Logged"
        return super().handle(request)



handlers = [
    authenticate,
    authorize,
    validate,
    process_request
]

for handler in handlers:

    result = handler(request)

    if result is not None:
        return result


class QueryBuilder:

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def limit(self, count):
        self.limit_value = count
        return self


#   QueryBuilder()
#     .where("age > 18")
#     .order_by("name")
#     .limit(10)


class OrderService:

    def __init__(self):
        self.repository = SqlOrderRepository()


class OrderService:

    def __init__(self, repository):
        self.repository = repository


repository = SqlOrderRepository()

service = OrderService(repository)


service = OrderService(FakeOrderRepository())


from event_emitter import EventEmitter

def send_email(user):
    print(f"Email sent to {user}")


def write_audit_log(user):
    print(f"Audit log created for {user}")


events = EventEmitter()

events.on("user_registered", send_email)
events.on("user_registered", write_audit_log)


events.emit("user_registered", "bob")

