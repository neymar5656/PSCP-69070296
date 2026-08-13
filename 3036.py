"""asdadfkfjdfkd"""
import math

def solve(N):
    r = math.isqrt(N - 1) + 1        # แถวที่ N อยู่
    j = N - (r - 1) ** 2              # ตำแหน่งในแถว r
    
    if j % 2 == 0:                    # ตำแหน่งคู่ = สามเหลี่ยมหัวลง
        return 2 * r - 3
    else:                             # ตำแหน่งคี่ = สามเหลี่ยมหัวขึ้น
        return 2 * r - 2

n = int(input())
print(solve(n))