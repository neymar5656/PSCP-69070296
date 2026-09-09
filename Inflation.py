"""Inflation"""
n = float(input())
k = int(input())

for i in range(k):
    money = n*0.0381
    money = int(money * 100) / 100
    n += money

print(f"{n:.2f}")
