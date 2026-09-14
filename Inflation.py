"""Inflation"""

n = input()
k = int(input())

if "." in n:
    a, b = n.split(".")
    b = (b + "00")[:2]
else:
    a = n
    b = "00"

money = int(a) * 100 + int(b)

for _ in range(k):

    increase = money * 381 // 10000
    money += increase

print(f"{money // 100}.{money % 100:02d}")
