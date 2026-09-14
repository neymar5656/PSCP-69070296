"""dsfasfa"""
X, Y = map(int, input().split())

total = 0
jump = X
count = 0

while total < Y and jump > 0:
    total += jump
    count += 1
    jump -= 2

if total >= Y:
    print(count)
else:
    print(-1)
