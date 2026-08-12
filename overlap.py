"""overlapping"""
x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

overlap_x = min(x1 + w1, x2 + w2) - max(x1, x2)
overlap_y = min(y1 + h1, y2 + h2) - max(y1, y2)

if overlap_x > 0 and overlap_y > 0:
    print(overlap_x * overlap_y)
else:
    print("no overlapping")
