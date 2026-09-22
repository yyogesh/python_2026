# Single Responsibility Principle
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def save_to_file(self):
        with open("student.txt", "w") as file:
            file.write(self.name)

    def send_email(self):
        print("Sending email...")


# Student
#  ├── Student data
#  ├── Calculation
#  ├── File storage
#  └── Email


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class StudentCalculator:
    def calculate_average(self, student):
        return sum(student.marks) / len(student.marks)


class StudentRepository:
    def save(self, student):
        with open("student.txt", "w") as file:
            file.write(student.name)


class EmailService:
    def send(self, student):
        print(f"Email sent to {student.name}")


# Student
#    ↓
# StudentCalculator

# Student
#    ↓
# StudentRepository

# Student
#    ↓
# EmailService