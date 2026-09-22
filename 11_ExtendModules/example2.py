from functools import reduce
from operator import itemgetter

employees = [
    {'name':'Alice',  'dept':'Engineering', 'salary':90000},
    {'name':'Bob',    'dept':'Marketing',   'salary':70000},
    {'name':'Cara',   'dept':'Engineering', 'salary':95000},
    {'name':'Dave',   'dept':'HR',          'salary':60000},
    {'name':'Eve',    'dept':'Marketing',   'salary':75000},
    {'name':'Frank',  'dept':'Engineering', 'salary':85000},
]

TARGET_DEPT = 'Engineering'
RAISE_PCT   = 10

eng_only = filter(lambda emp: emp['dept'] == TARGET_DEPT, employees)
eng_only = list(eng_only)
print(eng_only)

with_raise = map(lambda emp: {**emp, 'salary': emp['salary'] * (1 + RAISE_PCT / 100)}, eng_only)
with_raise = list(with_raise)
print(with_raise)

ranked = sorted(with_raise, key=lambda emp: emp['salary'], reverse=True)
print(ranked)


total_payroll = reduce(lambda total, emp: total + emp['salary'], ranked, 0)
print(total_payroll)



print(f'=== {TARGET_DEPT} Department — After {RAISE_PCT}% Raise ===')
print(f'{"Name":<12}{"Old Salary":>20}{"New Salary":>20}')
print('-' * 38)

for emp, orig in zip(ranked, sorted(eng_only, key=itemgetter('salary'), 
reverse=True)):
    print(f"{emp['name']:<12}{orig['salary']:>20,}{emp['salary']:>20,}")
print('-' * 38)
print(f'{"TOTAL PAYROLL":<12}{total_payroll:>24,}')
# javascript {name: "Alice", dept: "Engineering", salary: 90000}
# obj = {...emp, salary: 1000}

# total_raise = reduce(lambda total, emp: total + emp['salary'], with_raise, 0)
# print(total_raise)