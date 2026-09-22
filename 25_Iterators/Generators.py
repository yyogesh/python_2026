# __iter__()
# __next__()

# yield

def numbers():
    yield 10
    yield 20
    yield 30

for number in numbers():
    print(number)



def get_numbers():
    return [10, 20, 30]


# def demo():
#     print("Start")

#     yield 10

#     print("Middle")

#     yield 20

#     print("End")


# g = demo()

# print(next(g))
# print(next(g))
# print(next(g))


def counter():
    value = 0

    while value < 3:
        value += 1
        yield value

for number in counter():
    print(number)



def demo():
    yield 10
    return 100

g = demo()

print(next(g))
print(next(g))



def numbers():
    yield 1
    yield 2
    yield 3


def all_numbers():
    yield from numbers()
    yield 4
    yield 5


print(list(all_numbers()))


