age = 10

if age >= 18:
    print("You are an adult.")
    print("Another print statement for adults.")
else:
    print("You are a minor.")


marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")


marks = 95

if marks >= 70:
    print("C")
elif marks >= 80:
    print("B")
elif marks >= 90:
    print("A")


balance = 5000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining:", balance)
else:
    print("Insufficient Balance")




username = "admin"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login Successful")
else:
    print("Invalid Credentials")




age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Can Vote")
    else:
        print("Not a citizen")
else:
    print("Under Age")



if age < 18:
    print("Under Age")
elif not citizen:
    print("Not a citizen")
else:
    print("Can Vote")


# x = 10
# x == 10 ? print("Equal") : print("Not Equal")


x = 10
print("Equal") if x == 10 else print("Not Equal")


if marks >= 40:
    result = "Pass"
else:
    result = "Fail"


salary = 50000

bonus = 5000 if salary > 40000 else 2000

print(bonus)


grade = "A" if marks > 90 else "B" if marks > 80 else "C"

if marks > 90:
    grade = "A"
elif marks > 80:
    grade = "B"
else:
    grade = "C"


status = 200

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")



choice = int(input("1.Add 2.Subtract: "))

match choice:
    case 1:
        print("Addition Selected")
    case 2:
        print("Subtraction Selected")
    case _:
        print("Invalid Choice")