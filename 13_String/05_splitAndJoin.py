# split — divide string into a list
s = 'Python is a great language'
print(s.split())              # ['Python','is','a','great','language']
print(s.split(' ', 2))        # ['Python','is','a great language']  — max 2 splits
print('a,b,c'.split(','))     # ['a', 'b', 'c']
print('a,,b'.split(','))      # ['a', '', 'b']  — empty string for double comma

# rsplit — split from the RIGHT
print('a.b.c.d'.rsplit('.', 1))   # ['a.b.c', 'd']  — split on last dot only
# splitlines — split on any line ending (\n, \r\n, \r)
multiline = 'line1\nline2\r\nline3'
print(multiline.splitlines())   # ['line1', 'line2', 'line3']


# partition — split into exactly 3 parts at FIRST separator
email = 'user@example.com'
local, sep, domain = email.partition('@')
print(local, sep, domain)   # user @ example.com


# join — THE RIGHT WAY to build strings from lists

words = ['Hello', 'World', 'Python']
print(' '.join(words))        # 'Hello World Python'
print('-'.join(words))        # 'Hello-World-Python'
print(''.join(words))         # 'HelloWorldPython'
print(', '.join(words))       # 'Hello, World, Python'


# join with non-string items — must convert first!
numbers = [1, 2, 3, 4, 5]
print(', '.join(str(n) for n in numbers))  # '1, 2, 3, 4, 5'

