'''coke'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

a1 = (d - ((d//b))) 
cal = a1*a +((d//b)* c)

if not d%b:
    print(int(cal + 1 ))
else:
    print(int(cal))
