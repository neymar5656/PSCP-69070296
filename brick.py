'''block'''
a = int(input())
b = int(input())
goal = int(input())

b = b*5

if a + b < goal:
    print(-1)
elif not b - goal:
    print(0)
elif b > goal:
    if b%goal and a :
        print(0)
    elif not b%goal and a>5:
        print(b)