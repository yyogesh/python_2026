value = input("Enter a value: ")
print("You entered:", int(value) +10)

value = int(input("Enter a value: "))
print("You entered:", value +10)

x = 10
x = "123abc"
x = False

# Type conversion Explicit type conversion
x = 10
y = str(x)
print(type(y))

print(1+ 2.0)  # Output: 3.0

print(True + 1)  # Output: 2

age = input("Enter your age: ")
age = int(age)  # Convert the input string to an integer
print("Your age is:", age)


raw = input("Enter 3 numbers separated by spaces: ")
a, b, c = raw.split()  # Split the input string into three parts
a = int(a)  # Convert the first part to an integer
b = int(b)  # Convert the second part to an integer
c = int(c)  # Convert the third part to an integer
print("First number:", a)
print("Second number:", b)
print("Third number:", c)