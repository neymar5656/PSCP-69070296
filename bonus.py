"""bonus"""
role,years,salary = input().split()
salary = float(salary)
years = float(years)

if role == 'M':
    if years <= 5:
        ans = (salary*6/100)+1500
    elif 5 < years <= 10:
        ans = (salary*8/100)+1500
    else:
        ans = (salary*10/100)+1500
elif role == 'B':
    if years <= 5:
        ans = (salary*5/100)+1000
    elif 5 < years <= 10:
        ans = (salary*6/100)+1000
    else:
        ans = (salary*7/100)+1000
else:
    if years <= 5:
        ans = (salary*4/100)+500
    elif 5 < years <= 10:
        ans = (salary*5/100)+500
    else:
        ans = (salary*6/100)+500
print(int(ans))
