"""ความรักทำให้คนตาบอด"""
k = (input())
n = int(input())

first = n//2
for i in range(n):
    arrow = ""
    for h in range(i+1):
        arrow += k[h]

    print(arrow)
print(first)