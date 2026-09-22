# #Descriptors are the mechanism behind 
# themselves. Once you understand the protocol, you can build reusable, self-validating
# attributes that work across any number of classes.


# A descriptor is just an ordinary class that defines 
# __get__ , 
# __set__ , and/or 
# __delete__ . What
# makes it a ‘descriptor’ in the protocol sense is where it's placed: as a class attribute. Python's
# attribute lookup machinery checks for these methods and calls them instead of doing a normal
# __dict__ lookup.

class LoggedAttribute:
    """A descriptor that logs every get and set."""
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # accessed on the class itself, e.g. MyClass.attr
        print(f'GET {self.name} -> {obj.__dict__.get(self.name)}')
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        print(f'SET {self.name} = {value!r}')
        obj.__dict__[self.name] = value

class Widget:
    size = LoggedAttribute('size')
    def __init__(self):
        self.size = None

w = Widget()
w.size = 42          
print(w.size)   