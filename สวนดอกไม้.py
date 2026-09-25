"""AFadfdffffff"""
L, N = map(int, input().split())

d = 0
total = 0

while total < N:
    d += 1
    total += d

band = (d + L - 1) // L

print(band)
