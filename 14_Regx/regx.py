import re

# search
# match
# findall
# finditer
# sub
# split


email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
email = [
    '8d9m2@example.com',
    'not_an_email',
    'another_not_an_email',
    'yet_another_not_an_email',
]

for e in email:
    print(re.search(email_pattern, e))


text = "My phone number is 9876543210"

result = re.search(r"\d+", text)
print(result.group())


text = "I have 10 apples, 20 oranges and 30 bananas."

numbers = re.findall(r"\d+", text)

print(numbers)



text = "Python is easy and powerful"

words = re.findall(r"\w+", text)

print(words)


email = "user@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")


# sub  Replace all occurrences of a pattern with a replacement string

text = "Python is difficult"

new_text = re.sub(r"difficult", "easy", text)

print(new_text)


text = """
Name: Amit
Age: 35
Email: amit@gmail.com
Phone: 9876543210
"""


name = re.search(r"Name:\s*(.+)", text).group(1)
age = re.search(r"Age:\s*(\d+)", text).group(1)
email = re.search(r"Email:\s*([\w.-]+@[\w.-]+\.\w+)", text).group(1)
phone = re.search(r"Phone:\s*(\d{10})", text).group(1)

print(name)
print(age)
print(email)
print(phone)


# re.search()     → find first match
# re.match()      → match from beginning
# re.findall()    → find all matches
# re.finditer()   → iterate through matches
# re.sub()        → replace matches
# re.split()      → split using a pattern
# re.fullmatch()  → entire string must match


pattern = re.compile(r"\d+")
print(pattern.search("one1two2three3four4"))


# ── Validation patterns ──────────────────────────────────────
# Email validation
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
emails = ['valid@example.com','also.valid@sub.domain.in','invalid@','no-atsign']

for e in emails:
    result = 'VALID' if email_pattern.fullmatch(e) else 'INVALID'
    print(f'{e:<30} {result}')
    
# Indian mobile number (10 digits starting with 6-9)
mobile_pattern = re.compile(r'^[6-9]\d{9}$')
print(mobile_pattern.match('9876543210'))  # Match!
print(mobile_pattern.match('1234567890'))  # None  (starts with 1)
# Date format YYYY-MM-DD
date_pattern = re.compile(r'^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$')
print(bool(date_pattern.match('2024-03-15')))  # True
print(bool(date_pattern.match('2024-13-01')))  # False  (month 13 invalid)