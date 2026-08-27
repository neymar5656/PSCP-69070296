"""kuykuy"""
num, check = map(int, input().split())

diff = [0] * 1442

for _ in range(num):
    start, stop = map(int, input().split())

    diff[start] += 1
    diff[stop] -= 1

open_shop = [0] * 1441
open_shop[0] = diff[0]

for time in range(1, 1441):
    open_shop[time] = open_shop[time - 1] + diff[time]

checks = list(map(int, input().split()))

answers = []

for i in range(check):
    answers.append(str(open_shop[checks[i]]))

print(" ".join(answers))
