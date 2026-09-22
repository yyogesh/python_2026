print(7 /2)  # Output: 3.5
print(7 // 2)  # Output: 3
print(7 % 2)  # Output: 1

print(2 ** 3)  # Output: 8
# +, -, *, /, **, //, %


total_seconds = 245
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f'{minutes}:{seconds:02d}') # 9:5 # 9:05
print(17 % 2 == 0)  # Output: False
print(18 % 2 == 0)  # Output: True

for i in range(12):
    print(i % 4, end=" ")  # Output: 0 1 2 3 0 1 2 3 0 1 2 3


total_items = 23
per_page = 5
full_pages = total_items // per_page


last_page = total_items % per_page
total_pages = full_pages + (1 if last_page > 0 else 0)
print(f'Total pages: {total_pages}')  # Output: Total pages: 5

print(2 ** 3 ** 2)  # Output: 512 (2 raised to the power of (3 raised to the power of 2))
print( 8 ** (1/3))  # Output: 2.0 (cube root of 8)


# Logical operators
# and, or, not


# Relational operators
# ==, !=, >, <, >=, <=

print(10 == 10.0)  # Output: True
print(10 is 10.0)  # Output: False (different types, different objects)

print(True == 1)  # Output: True
print(False == 0)  # Output: True  

print('apple' < 'banana')  # Output: True (lexicographical comparison)

# ASCII values
print(ord('a'))  # Output: 97
print(ord('A'))  # Output: 65

print('Apple' < 'apple')  # Output: True (uppercase letters have lower ASCII values than lowercase letters)

x = 10

if x > 5 and x < 15:
    print("x is between 5 and 15")  # Output: x is between 5 and 15


# 18 <= age <= 65

print(18 <= x <= 65)


user = None

if user is None:
    print("No user logged in")  # Output: No user logged in

if user and user == 'Admin':
    print("Admin user logged in")


if not user:
    print("No user logged in")  # Output: No user logged in


# Truthy and Falsy values
# Falsy values: False, None, 0, 0.0, '', [], {}, set(), range(0)
# Truthy values: All other values

print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(''))  # Output: False
print(bool('Hello'))  # Output: True
print(bool([]))  # Output: False
print(bool([1, 2, 3]))  # Output: True
print(bool({}))  # Output: False
print(bool({1, 2, 3}))  # Output: True
print(bool(range(0)))  # Output: False
print(bool(range(5)))  # Output: True
print(bool([False]))  # Output: True


# Membership operators
# in, not in

print(10 in [1, 2, 3, 4, 5])  # Output: False
print(10 not in [1, 2, 3, 4, 5])  # Output: True

print('a' in 'apple')  # Output: True
print('a' not in 'apple')  # Output: False


# Identity operators
# is, is not

print(10 is 10)  # Output: True
print(10 is not 10)  # Output: False

print(10 is 10.0)  # Output: False
print(10 is not 10.0)  # Output: True

print(10 is 11)  # Output: False
print(10 is not 11)  # Output: True


# Operator precedence
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor division //, Modulo %
# 4. Addition +, Subtraction -
# 5. Left shift <<, Right shift >>
# 6. And &
# 7. Xor ^
# 8. Or |
# == != > < >= <=


result  = 2 + 3 * 4 ** 2 // 5 % 3 - 1
# Step 1: Exponentiation: 4 ** 2 = 16
# Step 2: Multiplication: 3 * 16 = 48
# Step 3: Floor division: 48 // 5 = 9
# Step 4: Modulo: 9 % 3 = 0
# Step 5: Subtraction: 2 + 48 - 1 = 50
print(result)  # Output: 50

# Bitwise operators
# &, |, ^, ~, <<, >>

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)  # Output: 1 (Binary: 0001)
print(a | b)  # Output: 7 (Binary: 0111)
print(a ^ b)  # Output: 6 (Binary: 0110)
print(~a)  # Output: -6 (Binary: 1010)
print(a << 2)  # Output: 20 (Binary: 10100)
print(a >> 2)  # Output: 1 (Binary: 0001)

