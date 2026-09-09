"""asdsadad"""
score = int(input())
bonus = int(input())
day = int(input())
Status = ''
#find score
if day > 3:
    result = (score + bonus)*1.5
else:
    result = (score + bonus)

if result >= 1500:
    Status = '5'
elif 1500 > result >= 1000:
    Status = '4'
elif 1000 > result >= 500:
    Status = '3'
elif 500 > result >= 200:
    Status = '2'
elif 200 > result:
    Status = '1'

if Status == '5' and day >= 7:
    Unique = '99'
elif Status == '4' and bonus > 300:
    Unique = '88'
else:
    Unique = '0'

print(int(result))
print(Status)
print(Unique)
