'''coke'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d == 0 or b == 0:
    print(a * d)
elif b == 1:
    print(a + c * (d - 1))
else:
    lo, hi = 1, d
    while lo < hi:
        mid = (lo + hi) // 2
        if mid + (mid - 1) // (b - 1) >= d:
            hi = mid
        else:
            lo = mid + 1
    print(a * lo + c * (d - lo))
