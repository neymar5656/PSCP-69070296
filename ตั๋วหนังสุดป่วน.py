"""wjle"""
n = int(input())
price = 0

while n > 0:
    age ,ticket = input().split()
    age = int(age)
    ticket = int(age)
    if age < 15:
        print('-1')
    elif ticket > n:
        print('-2')
    else:
        if 15 <= age <= 22:
            price += (150 * n)*0.2
        elif age <=60:
            price += (150 * n)*0.5
        else:
            price += (150 * n)
    print(price)
