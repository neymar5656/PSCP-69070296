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
        first_cost = (b * a) + c
        rem = d - (b + 1)
        sets = rem // b
        leftover = rem % b
        set_cost = ((b - 1) * a) + c
        
        total = first_cost + (sets * set_cost) + (leftover * a)
        print(total)