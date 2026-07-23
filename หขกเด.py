'''season'''
month = input()
day = int(input())

if month in ('1','2'):
    print('winter')
elif month == '3':
    if day < 21:
        print('winter')
    elif day >= 21:
        print('spring')

if month in ('3','4'):
    print('spring')
elif month == '6':
    if day < 21:
        print('spring')
    elif day >= 21:
        print('summer')

if month in ('7','8'):
    print('summer')
elif month == '9':
    if day < 21:
        print('summer')
    elif day >= 21:
        print('fall')

if month in ('9','10'):
    print('fall')
elif month == '12':
    if day < 21:
        print('fall')
    elif day >= 21:
        print('winter')
