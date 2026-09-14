"""kuyyy"""
n ,word = input().split()
n = int(n)

C = n // 2

for row in range(n):
    line = ""

    for col in range(n):
        if col in (row, n - row - 1):
            if word == "#":
                line += "#"
            else:
                distance = abs(C - row)
                line += chr(ord(word) + distance)
        else:
            line += "-"

    print(line)
