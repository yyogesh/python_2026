# path 
# pathlib module is used to handle the file path in python. 
# It is a built-in module that provides classes representing filesystem paths with 
# semantics appropriate for different operating systems.

from pathlib import Path
path = Path('/home/user/docs/report.pdf')
print(path)

# path = "data/users/users.csv"

# Get the Current Working Directory (CWD)
current_dir = Path.cwd()
print(f"Current Directory: {current_dir}")

# Get the User's Home Directory
home_dir = Path.home()
print(f"Home Directory: {home_dir}")


base = Path("data")

file_path = base / "users" / "users.csv"

print(file_path)

# "data" + "/" + "users" + "/" + "users.csv"


if path.exists():
    print("Path exists")
else:
    print("Path does not exist")

path.is_file()  # Check if it's a file
path.is_dir()   # Check if it's a directory


path = Path("app.log")

print(path.stat())

path = Path("data/reports")

path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist


path = Path("23_OOPS")

for file in path.iterdir():
    print(file)


print("List of Python files in the directory:")

for file in path.glob("*.py"):
    print(file)


for file in path.rglob("*.py"):
    print(file)

print("** Read the content of a file ***")
path = Path("23_OOPS/notes.txt")

content = path.read_text()

print(content)


# file = Path("message.txt")

# file.write_text(
#     "Hello Python!",
#     encoding="utf-8"
# )

Path("old.txt").rename("new.txt")  # Rename a file


Path("old.txt").unlink()  # Delete a file

Path("data").rmdir()  # Delete a directory