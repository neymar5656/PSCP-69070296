'''block'''
a = int(input())
b = int(input())
goal = int(input())

b = b*5
if b > goal:
    if goal % 5 > a:
        print('-1')
    else:
        print(goal % 5)
elif a + b < goal:
    print('-1')
elif not b:
    print(goal)
else:
    print(goal - b)
