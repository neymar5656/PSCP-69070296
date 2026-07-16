'''Bill'''
num = float(input())

a = (num/100)*10

if a <= 50:
    B = 50
elif a > 1000:
    B = 1000
else:
    B = a

c = num + B
d = (c/100)*7
ans = c + d
print(f'{ans:.2f}')
