'''temp'''
num = float(input())
old = input()
new = input()

if old == "K":
    Ce = num - 273.15
elif old == "F":
    Ce = 5/9*(num-32)
elif old == 'R':
    Ce= (num - 491.67)*5/9
else:
    Ce = num

if new == "K":
    print(f"{Ce + 273.15:.2f}")
elif new == "F":
    print(f"{Ce* 9/5 + 32:.2f}")
elif new == 'R':
    print(f"{(Ce + 273.15)*9/5:.2f}")
elif new == 'C':
    print(f'{Ce:.2f}')
