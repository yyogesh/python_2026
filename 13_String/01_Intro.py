s = 'Hello, World!'
print(s[0])  # Output: 'H'
print(s[7])  # Output: 'W'

# s[8] = 'w'  # This will raise an error because strings are immutable

print(id(s))  # Output: memory address of the string
s = 'p' + s[1:] # create a new string with 'p' replacing the first character
print(s)
print(id(s))  # Output: memory address of the string

# Four quote styles — all create str objects
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single
spans multiple lines'''
s4 = """triple double
also multi-line"""

# When to use which
s5 = "it's a string"       # double: avoids escaping apostrophe
s6 = 'say "hello"'         # single: avoids escaping quotes
# Raw strings — backslashes are LITERAL (great for paths & regex)

path = r'C:\Users\Name\Documents'  # Raw string
regx = r'\d{3}-\d{2}-\d{4}'  # Raw string for regex pattern


# Escape sequences
print('line1\nline2')   # newline
print('col1\tcol2')    # tab
print('back\\slash')   # literal backslash


# IMMUTABILITY — every 'modification' creates a NEW string
s = 'hello'
original_id = id(s)
s = s.upper()               # s now points to a NEW string 'HELLO'
print(id(s) == original_id) # False — different object!


parts = ['Hello', 'World', 'Python']

for part in parts:
    print(part)  # Output: Hello, World, Python

a = ''

for part in parts:
    a += part + ' '  # Concatenation creates a new string each time


a = ' '.join(parts)