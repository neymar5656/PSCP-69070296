"""braindead"""
s = input()
n = int(input())

for index, arrow in enumerate(s):
    if arrow == "R":
        for i in range(n):
            print(" " * (2 * i) + "*" * (n - i))

        for i in range(n - 2, -1, -1):
            print(" " * (2 * i) + "*" * (n - i))

    else:
        for i in range(n):
            print(" " * (n - 1 - i) + "*" * (n - i))

        for i in range(n - 2, -1, -1):
            print(" " * (n - 1 - i) + "*" * (n - i))

    if index < len(s) - 1:
        print()
