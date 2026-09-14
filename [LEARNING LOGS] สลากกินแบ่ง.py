"""sgggg"""
t1 ,n1 = input().split()
t2 ,n2 = input().split()

if t2 == t1 and n2 == n1:
    print(1000000)
elif n1 == n2:
    print(100000)
elif t2 == t1 and n2[-3] == n1[-3]:
    print(2000)
elif t2 == t1 and n2[-2] == n1[-2]:
    print(1000)
elif t2 != t1 and n2[-3] == n1[-3]:
    print(200)
elif t2 != t1 and n2[-2] == n1[-2]:
    print(100)
elif t2 == t1:
    print(20)
else:
    print(0)
