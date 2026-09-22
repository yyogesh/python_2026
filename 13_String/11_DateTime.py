from datetime import datetime, date
now = datetime.now()
today = date.today()
# Format datetime inside f-string using format spec
print(f'{now:%Y-%m-%d}')           # 2024-03-15
print(f'{now:%d/%m/%Y}')           # 15/03/2024
print(f'{now:%H:%M:%S}')           # 14:30:25
print(f'{now:%Y-%m-%d %H:%M}')     # 2024-03-15 14:30
print(f'{now:%B %d, %Y}')          # March 15, 2024
print(f'{now:%A, %d %B %Y}')       # Friday, 15 March 2024
# Common format codes:
# %Y = 4-digit year    %m = 2-digit month   %d = 2-digit day
# %H = 24-hour         %I = 12-hour         %M = minutes
# %S = seconds         %p = AM/PM           %A = weekday name
# %B = month name      %j = day of year     %W = week number

# Practical: timestamp for file names
filename = f'report_{now:%Y%m%d_%H%M%S}.pdf'
print(filename)   # report_20240315_143025.pdf