"""bgdf"""
d1 = input().split()
r = int(d1[0])
c = int(d1[1])

d2 = input().split()
kr = int(d2[0])
kc = int(d2[1])

n = int(input())

inf = []
i = 0
while i < n:
    d3 = input().split()
    inf.append((int(d3[0]), int(d3[1])))
    i += 1

grid = []
i = 0
while i < r:
    row = []
    j = 0
    while j < c:
        row.append(0)
        j += 1
    grid.append(row)
    i += 1

for pt in inf:
    pr = pt[0]
    pc = pt[1]
    
    i = 0
    while i < r:
        j = 0
        while j < c:
            dr = abs(i - pr)
            dc = abs(j - pc)
            m = dr if dr > dc else dc
            
            val = 0
            if m == 0:
                val = 100
            elif m == 1:
                val = 60
            elif m == 2:
                val = 20
                
            if val > grid[i][j]:
                grid[i][j] = val
            j += 1
        i += 1

safe = 0
i = 0
while i < r:
    j = 0
    while j < c:
        if grid[i][j] == 0:
            safe += 1
        j += 1
    i += 1

print(safe)
print(str(grid[kr][kc]) + "%")
