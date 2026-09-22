# x == 10 ? true : false

x = 10
result = "true" if x == 10 else "false"
print(result)

username = ''

display_name = username if username else "Guest"

temperature = 30
print("Hot") if temperature > 25 else print("Cold")

temperature = 30
print(f"Temperature is {'Hot' if temperature > 25 else 'Cold'}")

# nested ternary
marks = 75
grade = "A" if marks >= 90 else ("B" if marks >= 80 else ("C" if marks >= 70 else "D"))
print(grade)