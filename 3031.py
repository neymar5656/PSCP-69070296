"""I SUS I NAHEE"""
import math
hum ,lek = (map(int, input().split()))
PI = 3.1416

for _ in range(lek):
    x, y = map(int, input().split())
    if not x and not y:
        print(0)
        continue
    area = PI * (x**2 + y**2)
    time = area / hum
    print(math.ceil(time))
