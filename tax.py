"""car tax"""
year = int(input())
CC = int(input())

if year <= 1990:
    if CC <= 1500:
        print('1250')
    elif CC > 2000:
        print('2000')
    else:
        print('1400')
elif year >= 2000:
    if CC <= 1500:
        print('1000')
    elif CC > 2000:
        print('1500')
    else:
        print('1200')
else:
    if CC <= 1500:
        print('1100')
    elif CC > 2000:
        print('1700')
    else:
        print('1300')
