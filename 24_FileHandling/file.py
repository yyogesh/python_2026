import shutil


file = open("message.txt", "r")
print(file.read())
file.close()

# Mode	Meaning
# r	Read
# w	Write
# a	Append
# x	Create new file exclusively
# rb	Read binary
# wb	Write binary

with open("message.txt", "r") as file:
    print(file.read())

with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Hello")


with open("message.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line")


with open("data.txt", encoding="utf-8") as file:
    line = file.readline()

print(line)


# [
#     "First line\n",
#     "Second line\n",
#     "Third line\n"
# ]


with open("large.log", encoding="utf-8") as file:
    for line in file:
        print(line)



lines = [
    "Python\n",
    "Java\n",
    "C#\n"
]

with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)



with open("data.txt", "r", encoding="utf-8") as file:
    print(file.tell())


with open("data.txt", "r", encoding="utf-8") as file:
    file.seek(10)

    data = file.read()

print(data)

# 0
# ↓
# H e l l o   P y t h o n
#           ↑
#         position


# Buffer 


with open("photo.jpg", "rb") as file:
    data = file.read()


with open("original.pdf", "rb") as source:
    data = source.read()

with open("copy.pdf", "wb") as destination:
    destination.write(data)


shutil.copyfile("original.pdf", "copy.pdf")  # Copy file 