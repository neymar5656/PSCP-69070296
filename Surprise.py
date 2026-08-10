'''surprise'''
num1 = float(input())
num2 = float(input())

n = max(0.0,num1 - 2 * num2)
print(n)
if num2 - n > 2.0 :
    print('Surprising')
else:
    print('Not surprising')
