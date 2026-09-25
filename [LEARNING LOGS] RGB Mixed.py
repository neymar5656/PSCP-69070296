"""ASdasdasddaa"""
rgb1 = list(map(int, input().split()))
rgb2 = list(map(int, input().split()))

result = [(rgb1[i] + rgb2[i]) // 2 for i in range(3)]

print(*result)
