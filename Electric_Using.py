"""messi"""
from decimal import Decimal, ROUND_HALF_UP

n = int(input())
price = 0
for i in range(n):
    if i+1 <= 10:
        price += 5
    elif 10 < i+1 <=50:
        price += 7
    elif 50 < i+1 <=100:
        price += 10
    elif 100 < i+1 <=200:
        price += 12
    elif i+1 > 200:
        price += 15

ft = n*0.5
VAT = price*0.07
total = price + ft + VAT
total_decimal = Decimal(str(total))
ans = total_decimal.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

print(ans)
