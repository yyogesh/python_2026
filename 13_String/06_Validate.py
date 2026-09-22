# These return True/False — test the content of the string
print('123'.isdigit())        # True   — all digits 0-9
print('12.3'.isdigit())       # False  — decimal point fails
print('abc'.isalpha())        # True   — all letters
print('abc123'.isalnum())     # True   — letters AND digits
print('   '.isspace())        # True   — all whitespace
print('my_var'.isidentifier())# True   — valid Python name
print('MyClass'.isupper())    # False  — not ALL upper
print('HELLO'.isupper())      # True
print('hello'.islower())      # True
print('Hello World'.istitle())# True
print('Hello'.istitle())      # False