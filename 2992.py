'''shuffle'''
num = input()
gg = input()

B = num[1] + num[0]
c = int(B)
d = int(num)

if gg == '+':
    print(f'{num} + {c} = {d + c}')
elif gg == '*':
    print(f'{num} * {c} = {d * c}')
