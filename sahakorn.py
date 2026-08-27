"""sahakorn"""
import math
mem = input()
n = int(input())
price = 0
last_price = 0

for _ in range(n):
    price += float(input())

if mem == 'Y':
    last_price = price - price*0.05
elif mem == 'N':
    if price >= 500:
        last_price = price - price*0.03
    else:
        last_price = price

print(f"{(math.ceil(last_price * 100) / 100):.2f}")
