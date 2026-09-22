def countdown(n): #3 #2 #1 #0
    if n <= 1:
        return 1
    # print(n)
    return n * countdown(n-1) #2 #1 #0
# n * countdown(n-1) * countdown(n-2) * countdown(n-3) * countdown(n-4) * countdown(n-5) * countdown(n-6) * countdown(n-7) * countdown(n-8) * countdown(n-9) * countdown(n-10) * countdown(n-11) * countdown(n-12) * countdown(n-13) * countdown(n-14) * countdown(n-15) * countdown(n-16) * countdown(n-17) * countdown(n-18) * countdown(n-19) * countdown(n-20)

print(countdown(5)) #countdown(5)

# countdown(5)
#     ↓
# countdown(4)
#     ↓
# countdown(3)
#     ↓
# countdown(2)
#     ↓
# countdown(1)
#     ↓
# countdown(0)
#     ↓
# STOP

# LIFO — Last In, First Out


# ┌──────────────┐
# │ countdown(1) │
# ├──────────────┤
# │ countdown(2) │
# ├──────────────┤
# │ countdown(3) │
# └──────────────┘

# ┌──────────────┐
# │ countdown(0) │ ← current
# ├──────────────┤
# │ countdown(1) │
# ├──────────────┤
# │ countdown(2) │
# ├──────────────┤
# │ countdown(3) │
# └──────────────┘


# countdown(0) → finishes
#       ↑
# countdown(1) → finishes
#       ↑
# countdown(2) → finishes
#       ↑
# countdown(3) → finishes


# countdown(3)
# countdown(2)
# countdown(1)
# countdown(0)
#        ↓
#     return
#        ↑
#     return
#        ↑
#     return




        #       RECURSION

        #   ┌─────────────┐
        #   │   CALL      │
        #   └──────┬──────┘
        #          ↓
        #   Make problem
        #      smaller
        #          ↓
        #   ┌─────────────┐
        #   │ CALL AGAIN  │
        #   └──────┬──────┘
        #          ↓
        #         ...
        #          ↓
        #   ┌─────────────┐
        #   │ BASE CASE   │
        #   │    STOP     │
        #   └──────┬──────┘
        #          ↑
        #       RETURN
        #          ↑
        #       RETURN
        #          ↑
        #       RETURN

# Mental model: "Keep making the problem smaller until I can stop."

# Python remembers all the unfinished calls while I go deeper.



def fun(n):

    if n == 0:
        return

    print("Before", n)

    fun(n - 1)

    print("After", n)

fun(3)



# fun(3)

# Going Down

# fun(3)
#   Before 3

# fun(2)
#   Before 2

# fun(1)
#   Before 1

# fun(0)

# At this point:

# STOP

# Coming Back

# Now fun(1) continues after:

# fun(n - 1)

# So:

# After 1

# Then fun(2) continues:

# After 2

# Then fun(3) continues:

# After 3

# Final output:

# Before 3
# Before 2
# Before 1
# After 1
# After 2
# After 3



def example(n):

    if n == 0:
        return

    print(n)
    example(n - 1)

example(3) # 3 2 1
def example1(n):

    if n == 0:
        return

    example1(n - 1)
    print(n)

example1(3) # 1 2 3



def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))


#Python is simply storing unfinished function calls on the call stack.


def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

factorial(4)

# return n * factorial(n - 1) ==> 4 × ?

# I still need to calculate:

# 4 × ?


# Then factorial(3) needs:

# 3 × ?

# Then factorial(2) needs:

# 2 × ?

# def test(n):
#     print(n)
#     test(n - 1)


# def test(n):

#     if n == 0:
#         return

#     test(n + 1)

