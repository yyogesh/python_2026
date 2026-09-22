s = 'hello World PYTHON'
print(s.upper())       # 'HELLO WORLD PYTHON'
print(s.lower())       # 'hello world python'
print(s.title())       # 'Hello World Python'  — capitalise each word
print(s.capitalize())  # 'Hello world python'  — only first letter
print(s.swapcase())    # 'HELLO wORLD python'  — swap each letter's case
print(s.casefold())    # 'hello world python'  — aggressive lower (handles  unicode)


s = 'Hello World Hello Python'

# find — returns index of FIRST occurrence, -1 if not found
print(s.find('Hello'))          # 0
print(s.find('Hello', 1))       # 12  — start searching from index 1
print(s.find('xyz'))            # -1  — not found, no error


# rfind — returns index of LAST occurrence, -1 if not found
print(s.rfind('Hello'))         # 12
print(s.rfind('Hello', 1))      # 12  — start searching from index 1
print(s.rfind('xyz'))           # -1  — not found, no error


# www.google.com

# index — same as find but raises ValueError if not found
print(s.index('World'))         # 6
# print(s.index('xyz'))        ← ValueError!

# rfind / rindex — search from the RIGHT
print(s.rfind('Hello'))         # 12  — LAST occurrence
print(s.rindex('Hello'))        # 12  — LAST occurrence, raises ValueError if not found


# count — how many times substring appears
print(s.count('Hello'))         # 2
print(s.count('l'))             # 5


# startswith / endswith — check beginning or end
print(s.startswith('Hello'))    # True
print(s.startswith('World'))    # False
print(s.endswith('Python'))     # True


filename = 'photo.jpg'

print(filename.endswith(('.jpg','.jpeg','.png','.gif')))

print('jpg' in filename)  # True
print('txt' in filename)  # False

# 'in' — fastest for simple membership check
print('World' in s)             # True
print('xyz' not in s)           # True