# O(1) ==> constant time
# O(n) ==> linear time
# O(n^2) ==> quadratic time

#  Task: Find 'Sharma, Arjun' in a phonebook with n=10,000 pages
#   Strategy A: Read every single page until you find it
#     → 10,000 pages, 10,000 reads in the worst case
#     → If phonebook doubles to 20,000 pages → needs 20,000 reads
#     → Work grows LINEARLY with n → This is O(n)


# | Big-O          | Simple meaning                           | Python example             | If `n` becomes 10× larger          |
# | -------------- | ---------------------------------------- | -------------------------- | ---------------------------------- |
# | **O(1)**       | Work stays the same                      | `lst[0]`, `dct[key]`       | Same amount of work                |
# | **O(log n)**   | Problem is repeatedly divided            | Binary search              | Grows very slowly                  |
# | **O(n)**       | Look at each item once                   | `for x in data:`           | ~10× work                          |
# | **O(n log n)** | Divide + process items                   | `sorted(data)`             | ~10× plus a small extra factor     |
# | **O(n²)**      | Compare every item with every other item | Nested loops               | ~100× work                         |
# | **O(2ⁿ)**      | Number of possibilities doubles          | Naive recursive Fibonacci  | Explodes very quickly              |
# | **O(n!)**      | Generate every possible arrangement      | `itertools.permutations()` | Becomes enormous extremely quickly |

numbers = [10, 20, 30, 40, 50]

print(numbers[0])

user = {
    "name": "Yogesh",
    "age": 40
}

print(user["name"])

from bisect import bisect_left

sorted_list = [1, 3, 5, 7, 9]
index = bisect_left(sorted_list, 5)
print(index)


numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


numbers = [50, 10, 40, 20, 30]

numbers.sort()

# O(n log n) — divide + process items

# n * log n 

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    for j in numbers:
        print(i, j)

from functools import lru_cache
# def fibonacci(n):
#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


#O(n!)      Factorial    Impossible: 1,000,000! operations


# EVERY one of these is O(1) — instant, regardless of list size
lst = [10, 20, 30, 40, 50]
x = lst[0]           # O(1) — index access: direct memory calculation
x = lst[-1]          # O(1) — negative index: same direct calculation
x = lst[2]           # O(1) — ANY index: always exactly 1 operation
lst.append(99)       # O(1) amortised — add to end (no shifting needed)
lst.pop()            # O(1) — remove from end (no shifting needed)
length = len(lst)    # O(1) — Python stores length as an attribute
# Dictionary and set lookups are also O(1)
d = {'a': 1, 'b': 2}
x = d['a']           # O(1) — hash lookup
x = d.get('z', 0)    # O(1) — hash lookup with default
'a' in d             # O(1) — hash membership test
s = {1, 2, 3}
3 in s               # O(1) — hash membership (use sets, not lists!)
# Why is lst[i] O(1)? Because Python knows where item i is:
# address = base_address + (i * pointer_size)
# This is ONE calculation, regardless of i or list size

#*********************************************************

numbers = list(range(1_000_000))
# O(n) — must check every element in worst case
total = 0
for n in numbers:          # loop runs n times
    total += n
# These built-ins are also O(n) — they loop under the hood
result = sum(numbers)      # O(n) — adds each element once
maximum = max(numbers)     # O(n) — checks each element once
minimum = min(numbers)     # O(n) — checks each element once
found = 42 in numbers      # O(n) — list membership: scans each element
idx = numbers.index(999)   # O(n) — finds first occurrence: scans
count = numbers.count(1)   # O(n) — counts occurrences: full scan
copy = numbers.copy()      # O(n) — must copy each element
new_lst = numbers + [1]    # O(n) — creates a new list, copies all
# HOW TO SPOT O(n):
# ONE loop that runs n times, with O(1) work inside each iteration
# If the inner work is also O(n), the whole thing becomes O(n²)!
# PROOF — time grows linearly:
import timeit
for size in [1000, 10000, 100000]:
    t = timeit.timeit(lambda: sum(range(size)), number=100)
    print(f'n={size:>7}: {t:.3f}s')   # times roughly 10x each step


#*********************************************************

# O(n²) — a loop inside a loop over the same data
def has_duplicate_naive(lst):
    for i in range(len(lst)):         # outer loop: n times
        for j in range(i+1, len(lst)):# inner loop: up to n times
            if lst[i] == lst[j]:      # n * n/2 ≈ O(n²) comparisons
                return True
    return False
# For n=1000:   ~500,000 comparisons
# For n=10000:  ~50,000,000 comparisons (100x more work for 10x more data!)
# For n=100000: ~5,000,000,000 comparisons (EXTREMELY slow)
# O(n) alternative — using a set:
def has_duplicate_fast(lst):
    seen = set()
    for item in lst:     # one loop: O(n)
        if item in seen: # set lookup: O(1)
            return True
        seen.add(item)   # set add: O(1)
    return False
# Total: O(n) × O(1) = O(n) — massively faster!
# Bubble sort is also O(n²) — classic example
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):           # outer: n passes
        for j in range(n-i-1):  # inner: n-i comparisons
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
# Python's built-in sort is O(n log n) — always prefer it!


#Binary search — O(log n)
def binary_search(sorted_lst, target):
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_lst[mid] == target:
            return mid          # found!
        elif sorted_lst[mid] < target:
            left = mid + 1     # target in RIGHT half — discard left
        else:
            right = mid - 1    # target in LEFT half — discard right
    return -1   # not found
# Each iteration halves the search space:
# n=1,000,000 items: max 20 iterations
# vs linear search:  max 1,000,000 iterations
# Python's bisect module: binary search built in
import bisect
sorted_data = [1, 3, 5, 7, 9, 11, 13]
pos = bisect.bisect_left(sorted_data, 7)   # O(log n) search
print(pos)   # 3

# LIST 