"""gsfdgvsdfv"""
n = int(input())

most = []
for _ in range(n):
    a = int(input())
    b = int(input())
    most.append(max(a, b))

if n == 1:
    print(most[0])
else:
    total = sum(most)
    B = " + ".join(map(str, most))
    print(f"{B} = {total}")
