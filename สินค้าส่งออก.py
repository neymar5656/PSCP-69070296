"""hello"""
Sum = 0
Even = 0
Odd = 0

for i in range(int(input())):
    num = int(input())
    Sum += num
    if num % 2:
        Odd += 1
    elif not num % 2:
        Even += 1

print(f"SUM {Sum}")
print(f"EVEN {Even}")
print(f"ODD {Odd}")
