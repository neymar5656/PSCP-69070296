"""arrow"""

k = int(input())
n = (int(input()) - 1) // 2

dot = "*" * k
space = n
for i in range(n):
    print(f"{" " * space}{dot}")
    space -= 1

    i += 1

print(dot)
newspace = space + 1

for i in range(n):
    print(f"{" " * newspace}{dot}")
    newspace += 1

    i += 1
