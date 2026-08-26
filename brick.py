'''block'''
a = int(input())
b = int(input())
goal = int(input())

b = b*5

if goal % b != 0:
    print(goal % b)
elif b > goal:
    print('0')
elif a + b < goal:
    print('-1')
elif not b:
    print(goal)

else:
    print(goal - b)
