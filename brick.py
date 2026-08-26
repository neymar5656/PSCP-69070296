'''block'''
a = int(input())
b = int(input())
goal = int(input())

b = b*5

if b > goal:
    print('0')
elif a + b < goal:
    print('-1')
else:
    print(goal - b)
