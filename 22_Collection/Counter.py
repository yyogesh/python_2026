from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 3, 3]

print(nums.count(3))


count = {}

for num in nums:
    if num not in count:
        count[num] = 0

    count[num] += 1

print(count)


count = Counter(nums)
print(count)

print(count.most_common(1))

print(count.most_common(1)[0][0])

print(count.most_common(1)[0][1])

print(count.most_common(2))


s = "banana"

count = Counter(s)

print(count)

# O(n)

# Top K Frequent Elements

nums = [1, 1, 1, 2, 2, 3]

k = 2

count = Counter(nums)

answer = [x for x, freq in count.most_common(k)]

# for x, freq in count.most_common(k):
#     # answer.append(x)

print(answer)

# Contains Duplicate

nums = [1, 2, 3, 1]

print(Counter(nums).most_common(1)[0][1] > 1)

print(len(nums) != len(set(nums)))

#Valid Anagram

s = "anagram"

t = "nagaram"

# "listen"
# "silent"

print(sorted(s) == sorted(t))

print(Counter(s) == Counter(t))


#First Non-Repeating Character

s = "leetcode"

s = "aabbcdd"

# a → 2
# b → 2
# c → 1 ← first
# d → 2

for char in s:
    if s.count(char) == 1:
        print(char)
        break


# Find Missing Characters

s = "aabbccdde"

# a,b,c,d,e

count = Counter(s)

for char, frequency in count.items():
    print(char, frequency)

# a 2
# b 2
# c 2
# d 2
# e 1