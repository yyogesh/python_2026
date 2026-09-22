s = 'Python is great'
# Single index
print(s[0])      # 'P'  — first character
print(s[-1])     # 't'  — last character
print(s[7])      # 'i'

# Slicing s[start:end:step]

# start inclusive, stop EXCLUSIVE
print(s[0:6])    # 'Python'
print(s[7:9])    # 'is'
print(s[:6])     # 'Python'   — start defaults to 0
print(s[7:])     # 'is great' — stop defaults to end
print(s[-5:])    # 'great'    — last 5 characters
print(s[::2])    # 'Pto sget' — every second character
print(s[::-1])   # 'taerg si nohtyP' — reversed!

print(s[0:100]) 

print(s[100:])

# print(s[100])  # This will raise an IndexError because the index is out of range




