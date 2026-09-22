n = 20
print(f"O(log n)  ≈ {round(__import__('math').log2(n))} steps")   # ≈ 4
print(f"O(n)      = {n} steps")                                     # 20
print(f"O(n log n)≈ {round(n * __import__('math').log2(n))} steps") # ≈ 86
print(f"O(n²)     = {n**2} steps")                                  # 400
print(f"O(2ⁿ)     = {2**n} steps")                                  # 1,048,576
print(f"O(n!)     = astronomically large — don't even print it")


import bisect

sorted_nums = list(range(1_000_000))
# bisect does binary search: it cuts the search space in half each step
idx = bisect.bisect_left(sorted_nums, 999_999)   # O(log n) ≈ 20 steps, not 1,000,000


import timeit

big_list = list(range(1_000_000))
big_set  = set(range(1_000_000))

list_time = timeit.timeit(lambda: 999_999 in big_list, number=100)
set_time  = timeit.timeit(lambda: 999_999 in big_set,  number=100)

print(f"List search: {list_time:.5f} sec")
print(f"Set search:  {set_time:.5f} sec")


words = ["word"] * 100_000

def slow_concat():
    r = "" # string concatenation is O(n²) because strings are immutable
    for w in words:
        r += w #wordwordword
    return r

def fast_join():
    return "".join(words) # join is O(n)

print(timeit.timeit(slow_concat, number=10))   # noticeably slower
print(timeit.timeit(fast_join,  number=10))   # noticeably faster

#Repeated string concatenation in a loop can become inefficient because strings are immutable, 
# while join() is designed to combine multiple strings efficiently.


i = 0

while i < n:
    i += 2 # 2, 4, 6, 8, 10
    # 0 → 2 → 4 → 6 → 8 → 10 → ... → n

# O(n)


for i in range(n): # O(n)
    j = i

    while j < n: # O(log n)
        j *= 2 #1 → 2 → 4 → 8 → 16 → 32 → ... → n

# for loop → O(n)
# while loop → O(log n)
# O(n log n)



for i in range(n):
    for j in range(i):
        print(i, j)

# O(n^2)


result = []

for x in nums:
    if x not in result:
        result.append(x)

# O(n^2) because the "in" operation on a list is O(n), and this is nested inside a loop over nums.
# Space complexity: O(n)


