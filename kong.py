"""thailandfffffffff"""
W, L, M, N = map(int, input().split())

ans = float('inf')

for A in range(M, N + 1):
    waste = (W % A) * (L % A)
    ans = min(ans, waste)

print(ans)
