"""hbd"""
from datetime import date

y1, m1, d1 = (int(input()) for _ in range(3))
y2, m2, d2 = (int(input()) for _ in range(3))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

day = abs((date1 - date2).days)

if day <= 7:
    print('0')
elif date1 < date2:
    print('1')
else:
    print('2')
