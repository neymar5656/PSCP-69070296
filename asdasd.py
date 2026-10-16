"""hfasdgi"""
n, s = map(int, input().split())

students = [int(input()) for _ in range(n)]

visited = set()
current = s

while current != 0 and current not in visited:
    visited.add(current)
    current = students[current - 1]

print(len(visited))
