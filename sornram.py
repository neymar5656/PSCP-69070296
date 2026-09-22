"""ggez"""
k = int(input())
n = int(input())

gg = n//2

for i in range(n):
    ez = gg - abs(gg-i)
    print(" " * ez + "*" * k)
