n = int(input())

max_values = []
for _ in range(n):
    a = int(input())
    b = int(input())
    max_values.append(max(a, b))

if n == 1:
    print(max_values[0])
else:
    total = sum(max_values)
    equation = " + ".join(map(str, max_values))
    print(f"{equation} = {total}")
