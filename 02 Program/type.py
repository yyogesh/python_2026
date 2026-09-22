print(type(5))          # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("Hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))

# Print statement

# stack and heap memory
# class reference type


print("hello")
print(42)
print(3.14)
print(True)
print(None)

print("hello", 42, 3.14, True, None)

print("hello", end=" ")
print(42, end=" ")
print(3.14, end=" ")
print(True, end=" ")
print(None, end=" ")

print(10 + 5)
print(10 * 3 > 25)
print(len("Hello"))

name = "Alice"
age = 30
name = 20
print(name, age)

print("a", "b", "c", sep="-")

print("2024", "06", "30", sep="-")

print("home", "user", "documents", sep="/")

year, month, day = 2025, 12, 31

# year = 2025
# month = 12
# day = 31
print(year, month, day)

print(*'python', sep='-')  # This will raise an error because 'sep' is not a valid argument for print when only one string is provided.
# the * unpackes the string 'python' into individual characters, and sep='-' will separate them with a hyphen. The correct way to use it would be:

print("Name", end="\t")
print("Age", end="\t")
print("City", end="\n")
print("John", end="\t")
print(25, end="\t")
print("New York", end="\n")
print("Jane", end="\t")
print(30, end="\t")
print("London", end="\n")

# String formatting

name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# % formatting is an older method of formatting strings in Python. It uses placeholders like %s for strings and %d for integers, and the values are provided in a tuple after the % operator.
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
# python 3.6 introduced f-strings, which allow for inline expressions and variable interpolation using curly braces {}. They are more concise and readable than the older formatting methods.

print(f"My name is {name.upper()} and I am {age + 1} years old.")

# Tax calculation

price = 100
tax_rate = 0.075
tax = price * tax_rate
total = price + tax
print(f"Price: ${price:.2f}")
print(f"Tax: ${tax:.4f}")
print(f"Total: ${total:.2f}")

print(f'{price:10.2f}')  # Right-aligned with width 10
print(f'{price:<10.2f}')  # Left-aligned with width 10

# Integer formatting

number = 123456789
print(f'{number:,}')  # Output: 123,456,789
print(f'{number:,.2f}')  # Output: 123,456,789.00
print(f'{number:_}')  # Output: 123_456_789
print(f'{number:b}')  # Output: 111010110111100110100010101
print(f'{number:x}')  # Output: 75bcd15
print(f'{number:o}')  # Output: 232744064

# Alignment and width
text = "Hello"
print(f'{text:>10}')  # Right-aligned with width 10
print(f'{text:<10}')  # Left-aligned with width 10
print(f'{text:^10}')  # Center-aligned with width 10

print(f'{text:*^10}') 

# Percentage formatting
percentage = 0.1234
print(f'{percentage:.2%}')  # Output: 12.34%

#Sign formatting
positive_number = 42
negative_number = -42
print(f'{positive_number:+}')  # Output: +42
print(f'{negative_number:+}')  # Output: -42
