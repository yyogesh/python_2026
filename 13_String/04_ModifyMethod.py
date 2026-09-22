s = '  Hello, World!  '
# strip — remove leading AND trailing whitespace (default) or chars
print(repr(s.strip()))           # 'Hello, World!'
print(repr(s.lstrip()))          # 'Hello, World!  '  — left only
print(repr(s.rstrip()))          # '  Hello, World!'  — right only
print('###hello###'.strip('#'))  # 'hello'  — strip specific chars


# removeprefix / removesuffix  (Python 3.9+)
url = 'https://example.com'
print(url.removeprefix('https://'))    # 'example.com'
filename = 'report.pdf'
print(filename.removesuffix('.pdf'))   # 'report'


# replace — replace ALL occurrences (or limit with count)
text = 'cat cat cat'
print(text.replace('cat', 'dog'))          # 'dog dog dog'
print(text.replace('cat', 'dog', 2))       # 'dog dog cat'  — max 2


# Note: replace with empty string = delete
print('hello world'.replace(' ', ''))  # 'helloworld'

# expandtabs — replace tab with spaces
print('col1\tcol2\tcol3'.expandtabs(10))
