"""buzzing"""
num = int(input())

for i in range(num):
    i = i+1
    if not i % 15:
        i = 'FizzBuzz'
    else:
        if not i % 3:
            i = 'Fizz'
        elif not i % 5:
            i = 'Buzz'

    print(i)
