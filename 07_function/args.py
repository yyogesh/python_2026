def total(*numbers):
    print(f"Calculating total for: {numbers}")
    return sum(numbers)

print(total(1, 2,3,4,5))  # Output: 15
print(total(10, 20, 30))  # Output: 60

print(total(1, 2,3,4,5,6,7,8,9,10))  # Output: 55


def log(level, *messages):
    print(f"[{level}] {' '.join(messages)}")

log("INFO", "This is an info message.")
log("ERROR", "This is an error message.", "Please check the logs.") 
