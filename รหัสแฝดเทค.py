"""soory"""
n = int(input())
num1 = input().strip()
num2 = input().strip()

lek = 0

for i in range(n):
    og = int(num1[i]) + int(num2[i])
    if og != 9:
        lek += 1

if lek == 0:
    print("YES")
else:
    print(f"NO {lek}")
