'''surprise'''
num1 = float(input())
num2 = float(input())

n = num1 - 2 * num2
print(n)
print(num2 - n)
if num2 - n > 2.0 :
    print('Surprising')
else:
    print('Not surprising')
