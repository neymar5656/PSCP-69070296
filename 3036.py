"""การเหลี่ยม"""
N = int(input())

r = 1
while r * r < N:
    r += 1

ANUTIN = (r - 1)**2 + 1
CHAN = N - ANUTIN + 1
VIRAKUL = r - 1

if not CHAN % 2 :
    W = 1 + (VIRAKUL - 1) * 2
else:
    W = VIRAKUL * 2

print(W)
