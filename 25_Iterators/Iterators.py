# lazy evaluation

numbers = [10, 20, 30]

for number in numbers:
    print(number)


# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# __iter__ and __next__

print(numbers.__iter__())

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

# Iterable vs Iterator

numbers = iter([10, 20, 30])

print(list(numbers))


class CountUp:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            result = self.i
            self.i += 1
            return result
        else:
            raise StopIteration


for number in CountUp(5):
    print(number)