"""Chogath"""
check = ''
avg = 0
for i in range(int(input())):
    num = int(input())
    avg += num
    if num < 50:
        check = "FAIL"

result = avg/(i+1)

if result >= 60 and check != "FAIL":
    check = "PASS"
else:
    check = "FAIL"

print(f"{result:.1f}")
print(check)
