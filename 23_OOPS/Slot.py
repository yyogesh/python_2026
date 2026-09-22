#Every plain Python object normally carries a per-instance 
# __dict__ to hold its attributes —
# flexible, but expensive when you create millions of small objects. 
# __slots__ trades that
# flexibility for a fixed, compact attribute layout

class WithDict:
    def __init__(self, x, y):
        self.x, self.y = x, y


w = WithDict(1, 2)
print(w.__dict__)             
w.z = 99                       
print(w.__dict__)


class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y

s = WithSlots(1, 2)
print(s.x, s.y)
print(hasattr(s, '__dict__'))    # false   
try:
    s.z = 99                       
except AttributeError as e:
    print(f'Error: {e}')


import sys
class WithDict:
    def __init__(self, x, y):
        self.x, self.y = x, y

class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y


a, b = WithDict(1, 2), WithSlots(1, 2)
dict_total = sys.getsizeof(a) + sys.getsizeof(a.__dict__)
slots_total = sys.getsizeof(b)
print(f'dict-based: {dict_total} bytes')
print(f'slotted   : {slots_total} bytes')
print(f'saving    : {(1 - slots_total/dict_total)*100:.0f}%')


class Base:
    __slots__ = ('a',)

class Child(Base):
    __slots__ = ('b',)

c = Child()
c.a = 1
c.b = 2

print(c.a)
print(c.b)

class Child2(Base):
    pass

c2 = Child2()
c2.a = 1
c2.z = 100

print(hasattr(c2, '__dict__'))  # True