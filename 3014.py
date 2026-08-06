"""humlek"""
a, b, c, d = ((int(input()))for _ in range(4))

real_price = d//a

if not b or not c:
    print(real_price)
elif b == 1:
    E = real_price//b
    E = E*c
    sol = real_price + E
    print(sol- 1)
else:
    E = real_price//b
    E = E*c
    sol = real_price + E
    print(sol)
