print(abs(-10))  # Output: 10

print(all([True, True, False]))  # Output: False
print(any([True, True, False]))  # Output: True

print(bin(10))  # Output: '0b1010'

print(pow(2, 3))  # Output: 8

print(round(3.14159, 2))  # Output: 3.14

print(sum([1, 2, 3, 4, 5]))  # Output: 15


print(divmod(10, 3))  # Output: (3, 1)


print(hash("Hello"))  # Output: 123456

words = ["apple", "banana", "cherry"]
print(sorted(words))  # Output: ['apple', 'banana', 'cherry']

print(max(words, key=len))  # Output: 'cherry'
print(min(words))  # Output: 'apple'


dict = {"x": 1, "y": 2, "c": 3}

dict_a = {"z": 5}

expr = "x + y + z"

print(eval(expr, dict, dict_a))  # Output: 8


# type, isinstance, issubclass, dir, id, repr, str, format, vars, locals, globals, 
# callable, memoryview, bytearray, bytes, complex, float, int, list, tuple, set, frozenset, dict

# sorted, reversed, enumerate, zip, map, filter, reduce, all, any, sum, min, max, 
# abs, round, pow, divmod, hash, bin

# sum of two numbers

def add(a, b):
    return a + b

print(add(1, 2))