"""กระต่ายน้อย"""
n = int(input())
score = []
while n >0 :
    x = int(input())
    score.append(x)
    n -= 1
m = max(score)
n_m = score.count(m)
print(m)
print(n_m)
