x, k = input().split()
x = int(x)

center = x // 3

for row in range(x):
    line = ""

    for col in range(x):
        if col == row or col == x - row - 1:
            if k == "#":
                line += "#"
            else:
                distance = abs(center - row)
                line += chr(ord(k) + distance)
        else:
            line += "-"

    print(line)