# Index:     0    1    2    3    4
#           +----+----+----+----+----+
# Value:    | 10 | 20 | 30 | 40 | 50 |
#           +----+----+----+----+----+
numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # 10
print(numbers[3])   # 40


numbers[1] = 99
print(numbers[1])   # 99 # [10, 99, 30, 40]

# We did not create a completely new list.

# We changed an element inside the existing list.

# In-place means: modify the existing data instead of creating another
# copy of the data.

# Option A --- Erase and change the existing whiteboard

# 10 99 30 40

# This is similar to an in-place operation.

# Option B --- Buy another whiteboard

# Original:

# 10 20 30 40

# New:

# 10 99 30 40

# Now you have two copies.

# This generally uses extra memory.

# Java Array vs Python List

# Java Array:

# int[] numbers = new int[5];


numbers = [10, 20, 30]

new_numbers = [100, 20, 30]

print(numbers)
print(new_numbers)



numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers) # [4, 3, 2, 1]

#reverse() changes the original list. That is an in-place operation.

#reverse() vs reversed()

numbers = [1, 2, 3]

result = reversed(numbers)

print(list(result))

print(numbers)

# [3, 2, 1]
# [1, 2, 3]

#The original list remains unchanged.

# reverse()
#     ↓
# "Change this list."

# reversed()
#     ↓
# "Give me something that reads this list backwards."


numbers = [10, 20, 30]

numbers.append(40)

print(numbers) # [10, 20, 30, 40]

#The existing list was modified.

# append()
# extend()
# insert()
# remove()
# pop()
# sort()
# reverse()
# clear()

# Suppose we have:

# 1,000,000 elements

# Creating another complete list can require significant additional memory.

# An in-place algorithm tries to work with the existing storage.

# Rotate the array in-place.

#It is in-place, but reversing 1 million elements still requires work.

# Time:  O(n)
# Extra space: O(1)

# [10, 20, 30, 40, 50]

# The first element moves to the end.

[20, 30, 40, 50, 10]


[10, 20, 30, 40, 50]

# Left rotation

# 10 | 20 30 40 50
# ↓
# 20 30 40 50 | 10

# Right rotation

# 10 20 30 40 | 50
#               ↓
# 50 | 10 20 30 40


numbers = [10, 20, 30, 40, 50]

numbers =  numbers[1:] + [numbers[0]]

numbers =  numbers[1:] + numbers[:1]

print(numbers)


#Left Rotation by k Positions

# numbers = [10, 20, 30, 40, 50]

# Rotate left by 2.

numbers = [10, 20, 30, 40, 50]
k = 2

numbers = numbers[k:] + numbers[:k]

print(numbers)


# Use k % n? # 2 % 5

# Suppose there are 5 elements:

# [10, 20, 30, 40, 50]

# Rotating left by 5 means:

# [10, 20, 30, 40, 50]

# Rotating by 6 is the same as rotating by 1. 6 % 5 = 1

# k = k % len(numbers)

k = 7
n = 5

k = k % n

print(k)

7 % 5 = 2

# So rotating 7 positions is equivalent to rotating 2 positions.

numbers = [10, 20, 30, 40, 50]
k = 2

k = k % len(numbers)

numbers = numbers[-k:] + numbers[:-k]

print(numbers)


# The Reverse Technique

# For right rotation by k.

[10, 20, 30, 40, 50]

# [40, 50, 10, 20, 30]











