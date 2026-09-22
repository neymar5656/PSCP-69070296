"""wjle"""
n = int(input())

while n > 0:
    age ,ticket = input().split()
    age = int(age)
    ticket = int(ticket)
    if age < 15:
        print('-1')
        continue

    if ticket > n:
        print('-2')
        continue

    if 15 <= age <= 22:
        price = 120
    elif age >= 60:
        price = 75
    else:
        price = 150

    total = price*ticket
    n -= ticket

    print(total,n)
