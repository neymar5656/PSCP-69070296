"""humlek"""
a, b, c, d = (int(input()) for _ in range(4))

bottles = d // a
caps = bottles

if b > 0:
    while caps >= b:
        exchanges = caps // b
        got = exchanges * c
        bottles += got
        caps = caps % b + got
print(bottles)
