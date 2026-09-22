# calculator.py
# a simple calculator program that can perform basic arithmetic operations

# -- Step 1: Define functions for each operation --

print('=' * 40)
print('       PYTHON CALCULATOR v1.0') 
print('=' * 40)
print()

 
# ── Step 2: Get input from user ───────────────────────────── 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ── Step 3: Perform operations ──────────────────────────────

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


# division with error handling for division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# ── Step 4: Display results ────────────────────────────────
print()

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")


