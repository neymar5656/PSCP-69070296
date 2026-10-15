"""นดฟดหกอดฟห"""
s = input().strip()
u = ""
for ch in s:
    if 'a' <= ch <= 'z':
        u += chr(ord(ch) - 32)
    else:
        u += ch

allti = True
for ch in u:
    if ch != 'I' and ch != 'T':
        allti = False
        break

if allti and len(u) > 0:
    print("unknown " + str(len(u)))
else:
    inv = False
    idx = -1
    maxa = 0
    i = 0
    n = len(u)
    while i < n:
        ch = u[i]
        if ch == 'A':
            if i == 0 or (u[i-1] != 'R' and u[i-1] != 'A'):
                inv = True
                idx = i
                break
            i += 1
        elif ch == 'R':
            if i + 1 >= n or u[i+1] != 'A':
                inv = True
                idx = i + 1
                break
            i += 1
            cura = 0
            while i < n and u[i] == 'A':
                cura += 1
                i += 1
            if cura > maxa:
                maxa = cura
        elif ch == 'B':
            if i + 1 >= n or (u[i+1] != 'I' and u[i+1] != 'T'):
                inv = True
                idx = i + 1
                break
            i += 1
            while i < n and (u[i] == 'I' or u[i] == 'T'):
                i += 1
        elif ch == 'I' or ch == 'T':
            i += 1
        else:
            inv = True
            idx = i
            break

    if inv:
        print("no " + str(idx))
    else:
        print("yes " + str(maxa))