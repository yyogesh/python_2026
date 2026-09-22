day = 'Monday'
match day:
    case 'Monday':
        print('Today is Monday')
    case 'Tuesday':
        print('Today is Tuesday')
    case 'Wednesday':
        print('Today is Wednesday')
    case 'Thursday':
        print('Today is Thursday')
    case 'Friday':
        print('Today is Friday')
    case 'Saturday':
        print('Today is Saturday')
    case 'Sunday':
        print('Today is Sunday')
    case _:
        print('Invalid day')


match day:
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print('Today is a weekday')
    case 'Saturday' | 'Sunday':
        print('Today is a weekend')
    case _:
        print('Invalid day')




score = 85
match score:
    case n if n >= 90:
        print('Grade: A')
    case n if n >= 80:
        print('Grade: B')
    case n if n >= 70:
        print('Grade: C')
    case n if n >= 60:
        print('Grade: D')
    case _:
        print('Grade: F')


#tuple, dict, list pattern matching

point = (3, 4)
match point:
    case (0, 0):
        print('Origin')
    case (0, y):
        print(f'Y={y}')
    case (x, 0):
        print(f'X={x}')
    case (x, y):
        print(f'X={x}, Y={y}')


# in operator
fruits = ['apple', 'banana', 'orange']
match 'apple' in fruits:
    case True:
        print('Fruit found')
    case False:
        print('Fruit not found')