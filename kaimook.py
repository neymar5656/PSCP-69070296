"""kaimook"""
parung, kai = input().split()
cha, sweat, numcha = input().split()

kai = float(kai)
sweat = int(sweat)
numcha = float(numcha)

cal = 0
calcha = 0

if parung == 'H':
    cal = 5 * kai
elif parung == 'O':
    cal = 3 * kai
elif parung == 'J':
    cal = 2 * kai

if cha == 'R':
    if sweat == 1:
        calcha = 12
    elif sweat == 2:
        calcha = 18
    elif sweat == 3:
        calcha = 25
elif cha == 'T':
    if sweat == 1:
        calcha = 15
    elif sweat == 2:
        calcha = 20
    elif sweat == 3:
        calcha = 30
else:
    if sweat == 1:
        calcha = 10
    elif sweat == 2:
        calcha = 15
    elif sweat == 3:
        calcha = 20

calcha = calcha * numcha
result = cal + calcha

if result.is_integer():
    print(int(result))
else:
    print(result)