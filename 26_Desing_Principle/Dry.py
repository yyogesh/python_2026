def calculate_student1_marks():
    total = 80 + 75 + 90
    average = total / 3
    print("Average:", average)


def calculate_student2_marks():
    total = 70 + 85 + 95
    average = total / 3
    print("Average:", average)


calculate_student1_marks()
calculate_student2_marks()

# DRY
def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)


student1 = [80, 75, 90]
student2 = [70, 85, 95]

print("Student 1:", calculate_average(student1))
print("Student 2:", calculate_average(student2))