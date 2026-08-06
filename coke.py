'''coke'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b <= 1 or c == a or d == 0:
    print(a * d)
else:
    if d <= b:
        print(a * d)
    else:
        sets = (d - (b + 1))// b
        leftover = (d - (b + 1)) % b
        set_cost = ((b - 1) * a) + c
        
        total = ((b * a) + c) + (sets * set_cost) + (leftover * a)
        print(total)
