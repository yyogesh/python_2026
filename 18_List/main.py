#list set tuple dict

#list are ordered, mutable, allow duplicates
#tuple are ordered, immutable, allow duplicates
#set are unordered, mutable, no duplicates
#dict are unordered, mutable, no duplicates

#list methods
#append, insert, remove, pop, clear, count, index
# sort, reverse, copy

import sys


my_list = [42, 'hello', 3.14, True] # 8 bytes

my_list.append(4)

print(my_list)

a = my_list.copy()

print(a)

# DSA 
# MATH 

lst = []
for i in range(20):
    lst.append(i)
    print(f'length: {len(lst)}, capacity: {sys.getsizeof(lst)}')

# 1.125x

l2 = list((3, 5, 6, 8))
print(l2)

l3 = list('abcd')
print(l3)

print(l3[1])

l3[1] = 'z'
print(l3)


l3.remove('a')

print(l3)


lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.append(7)

lst.extend([8, 9, 10])

lst.insert(0, 0)

print(lst)

print(lst[0])
print(lst[-1])
print(lst[0:3])
print(lst[0:8:2])

print(lst.index(9))


print(lst.count(9))

lst.sort()
print(lst)

lst.reverse()
print(lst)

lst2 = lst.copy()
print(lst2)

lst.clear()
print(lst)

print(lst2)

print(4 in lst)


def safe_index(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

print(safe_index(lst2, 0))

print(safe_index(lst2, 50))


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing: lst[start:stop:step]
print(lst[2:7])          # [2, 3, 4, 5, 6]   — start incl, stop excl
print(lst[:5])           # [0, 1, 2, 3, 4]   — from beginning
print(lst[5:])           # [5, 6, 7, 8, 9]   — to end
print(lst[::2])          # [0, 2, 4, 6, 8]   — every second
print(lst[1::2])         # [1, 3, 5, 7, 9]   — odd indices
print(lst[::-1])         # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  — reversed
print(lst[7:2:-1])       # [7, 6, 5, 4, 3]   — backward with step


first, *middle, last = lst
print(first)  # Output: 0
print(middle)  # Output: [1, 2, 3, 4, 5, 6, 7]
print(last)  # Output: 8

a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)   # 1 2 [3, 4, 5]



lst = [0, 1, 2, 3, 4, 5]
lst[1:3] = [10, 20, 30]      # replace indices 1,2 with 3 items
print(lst)   # [0, 10, 20, 30, 3, 4, 5]
lst[2:5] = []                # delete a section
print(lst)   # [0, 10, 4, 5]
lst[::2] = [0, 0, 0]         # replace every second element
print(lst)   # [0, 10, 0, 5, 0]   # assignment must match count


# list, set, tuple, dict, oops, file handling, mutlithreading, async/await

# algo 
# DSA 


# Create a list of 10 numbers and calculate sum/min/max manually.
# Find the second-largest number.
# Count even and odd numbers.
# Remove all negative numbers.
# Find duplicate elements.
# Find unique elements without using set().
# Merge two lists.
# Find common elements between two lists.
# Rotate a list left/right.
# Reverse a list without using reverse() or slicing.



# Let's make the ATM support:

# Multiple bank accounts
# Card + PIN authentication
# Maximum 3 PIN attempts
# Account balance
# Deposit
# Withdrawal
# Daily withdrawal limit
# Transfer money to another account
# Mini statement / transaction history
# Change PIN
# Account information
# Logout
# Transaction IDs
# Validation for invalid amounts
# ATM cash availability
# Different transaction types
# Menu-driven transaction processing


accounts = {
    '1234': {
        'pin': '5678',
        'name': 'Arjun Mehta',
        'balance': 25000,
        'daily_withdrawal': 0,
        'transactions': []
    },

    '9876': {
        'pin': '4321',
        'name': 'Priya Sharma',
        'balance': 50000,
        'daily_withdrawal': 0,
        'transactions': []
    },

    '5555': {
        'pin': '9999',
        'name': 'Rahul Verma',
        'balance': 100000,
        'daily_withdrawal': 0,
        'transactions': []
    }
}