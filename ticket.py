'''Ticket'''
years_old = int(input())
A = str(input().upper())
Cost = 0
if years_old < 18:
    Cost += 20
elif years_old >= 18:
    if A == 'S':
        Cost += 20
    else:
        Cost += 50

print(Cost)
