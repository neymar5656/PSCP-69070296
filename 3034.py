"""pod"""
Num ,K = map(int, input().split())
count = [0] * (K + 1)

for _ in range(Num):
    left = int(input())
    count[left] += 1

kon = min(count[1:K+1])
kon = kon * K
ans = Num - kon
print(ans)
