"""i love dr sooksun"""
n = input()

a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])

if a > 5:
    FLOOR = 9
elif b > 5:
    FLOOR = 10
elif c > 5:
    FLOOR = 11
elif d > 5:
    FLOOR = 12
elif e > 5:
    FLOOR = 14
else:
    FLOOR = 13

PALINDROME = n == n[::-1]

if PALINDROME:
    if a + e > 5:
        SECOND = 1
    elif b * d > 5:
        SECOND = 2
    else:
        SECOND = 0
else:
    if e != 0 and a // e > 5:
        SECOND = 1
    elif b - e > 5:
        SECOND = 2
    else:
        SECOND = 0

total = a + b + c + d + e
product = a * b * c * d * e

if total > 25:
    THIRD = 1
elif product > 55:
    THIRD = 2
else:
    THIRD = 0

print(f"{FLOOR}{SECOND}{THIRD}")
