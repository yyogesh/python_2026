# BIG PROBLEM
#     ↓
# SMALLER PROBLEM
#     ↓
# SMALLER PROBLEM
#     ↓
# SMALLEST PROBLEM
#     ↓
# STOP
#     ↑
# RETURN
#     ↑
# RETURN
#     ↑
# FINAL ANSWER

#Python is simply keeping unfinished function calls on the call stack.

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(4))

def sum_even(n):
    if n == 0:
        return 0

    return n + sum_even(n - 2)


#F(n) = F(n - 1) + F(n - 2)

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
def fid(n):
    if n == 1 or n == 2:
        return 1

    return fid(n - 1) + fid(n - 2)

print(fid(6))
# f(4)
#  ↓
# f(3)
#  ↓
# f(2)
#  ↓
# f(1)


#        f(4)
#       /    \
#     f(3)   f(2)
#    /   \
#  f(2)  f(1)


#                     start
#                   /       \
#                take       skip
#               /    \      /   \
#            take    skip  take  skip


#Backtracking

# CHOOSE
#   ↓
# EXPLORE
#   ↓
# UNDO
#   ↓
# TRY NEXT


items = ["A", "B"]
# What subsets are possible?
[]
["A"]
["B"]
["A", "B"]

#                      []
#                    /    \
#               TAKE A    SKIP A
#                [A]        []
#               /   \      /   \
#          TAKE B SKIP B TAKE B SKIP B
#           [A,B]   [A]   [B]    []


def subsets(items): #["A", "B"]
    result = []

    def backtrack(index, current_subset):
        if index == len(items): # 0, 2
            result.append(current_subset.copy()) # [[], ["A"], ["B"], ["A", "B"]]
            return
# Choice 1: take the item
        current_subset.append(items[index]) # [['A', 'B']]
        print('current_subset', current_subset)
        backtrack(index + 1, current_subset) # 1, ['A']

        # Undo the choice
        current_subset.pop() # []

        # Choice 2: skip the item
        backtrack(index + 1, current_subset)

    backtrack(0, [])
    return result


print(subsets(["A", "B"]))


    #               START
    #                |
    #           MAKE CHOICE
    #                |
    #            RECURSE
    #                |
    #          DID IT FINISH?
    #           /          \
    #         YES           NO
    #          |             |
    #       RECORD        continue
    #          |
    #        UNDO
    #          |
    #     TRY NEXT CHOICE


#     Subsets
# Permutations
# Combinations
# Maze solving
# N-Queens
# Sudoku
# Path finding
# Word search
# Decision problems