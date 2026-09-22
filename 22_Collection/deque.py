from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.popleft()
print(q)



from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())


nums = deque([1, 2, 3, 4, 5])


# 1, 2, 3, 4, 5

# 5, 1, 2, 3, 4

# 4, 5, 1, 2, 3
nums.rotate(2)
print(nums)



# Sliding Window

nums = [1, 2, 3, 4, 5]

K = 3 

# [1 2 3]
#   [2 3 4]
#     [3 4 5]

# Palindrome Using