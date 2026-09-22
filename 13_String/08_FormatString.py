# f-strings: any Python expression inside {}
name = 'Arjun'
score = 87.456
items = ['apple', 'banana']
print(f'Hello {name}!')                    # Hello Arjun!
print(f'Score: {score:.2f}')              # Score: 87.46
print(f'Items: {len(items)}')             # Items: 2
print(f'Upper: {name.upper()}')           # Upper: ARJUN
print(f'Square: {4**2}')                  # Square: 16
# Debug with = (Python 3.8+)
x = 42
print(f'{x=}')           # x=42  — shows name AND value!
print(f'{name.lower()=}')# name.lower()='arjun'
# Format spec: {value:[[fill]align][sign][width][.precision][type]}
pi = 3.14159265
# Number formatting
print(f'{pi:.2f}')        # 3.14    — 2 decimal places
print(f'{pi:10.3f}')      #      3.142 — width 10, 3 decimals
print(f'{1234567:,}')     # 1,234,567  — thousands separator
print(f'{1234567:_}')     # 1_234_567  — underscore separator
print(f'{0.875:.1%}')     # 87.5%      — percentage
print(f'{255:08b}')       # 11111111   — binary, zero-padded to 8
print(f'{255:08x}')       # 000000ff   — hex, zero-padded
print(f'{1.23e6:.2e}')    # 1.23e+06   — scientific notation
# String / alignment formatting
word = 'Python'
print(f'{word:<20}|')     # 'Python              |'  left
print(f'{word:>20}|')     # '              Python|'  right
print(f'{word:^20}|')     # '       Python       |'  center
print(f'{word:*^20}|')    # '*******Python*******|'  custom fill