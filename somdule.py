"""mhaggg"""
n = int(input())

heavy = 0

for _ in range(n):
    h = int(input())

    if h > 18:
        heavy += 1

normal = n - heavy

days = n + max(0, heavy - normal - 1)

print(days)
