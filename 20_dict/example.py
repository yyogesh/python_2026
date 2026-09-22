import sys

n, data = 1000, list(range(1000))
print(f'list  : {sys.getsizeof(data):>8} bytes')
print(f'tuple : {sys.getsizeof(tuple(data)):>8} bytes')
print(f'set   : {sys.getsizeof(set(data)):>8} bytes   (~4x list)')
print(f'dict  : {sys.getsizeof({x:x for x in data}):>8} bytes   (~4.5x list)')
# DECISION GUIDE:
# Read-only ordered sequence   → tuple   (smallest, fastest iterate)
# Mutable ordered sequence     → list    (fast append/pop from end)
# Membership testing           → set     (O(1), worth the 4x memory)
# Key-value lookup             → dict    (O(1), worth the 4.5x memory)


from collections import Counter

c = Counter('abracadabra')
print(c)               # Counter({'a':5,'b':2,'r':2,'c':1,'d':1})
print(c['a'])          # 5
print(c['z'])          # 0  (no KeyError — missing = 0)
print(c.most_common(3))# [('a',5),('b',2),('r',2)]
# Counter arithmetic
c1 = Counter(['python','is','great','python'])
c2 = Counter(['python','rocks','great','rocks'])
print(dict(c1 + c2))   # add counts:    {'python':3,'great':2,'is':1,'rocks':2}
print(dict(c1 - c2))   # subtract +ve:  {'python':1,'is':1}
print(dict(c1 & c2))   # minimum:       {'python':1,'great':1}
print(dict(c1 | c2))   # maximum:       {'python':2,'great':1,'is':1,'rocks':2}
# update() adds; subtract() subtracts (can go negative)
c.update('aaa')         # adds 3 more 'a'
c.subtract('rrr')       # subtracts 3 'r' (r goes to -1)
print(c)
print(+c)               # + removes zero/negative counts