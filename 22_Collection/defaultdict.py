#defaultdict

data = {}

employees = {}

# employees["IT"].append("Amit")


employees = {}

if "IT" not in employees:
    employees["IT"] = []

employees["IT"].append("Amit")


from collections import defaultdict

employees = defaultdict(list) # employees = {}

employees["IT"].append("Amit")
employees["IT"].append("Rahul")
employees["HR"].append("Priya")

print(employees)

words = ["cat", "dog", "apple", "bat", "hello"]

groups = defaultdict(list)

for word in words:
    groups[len(word)].append(word)

print(groups)



#Group Anagrams

# ["eat", "tea", "tan", "ate", "nat", "bat"]

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word)) # ate -> aet
    groups[key].append(word)

print(groups)