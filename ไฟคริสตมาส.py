"""dogshit eeee"""
F,n = input().split()
n = int(n)

color = ["Red","Green","Blue"]

color_map = {'R': 0,'G':1, 'B':2}

color_map = {"R": 0, "G": 1, "B": 2}
start_index = color_map[F]

result = []
for i in range(n):
    current_index = (start_index + i) % 3
    result.append(color[current_index])

print(*result)
