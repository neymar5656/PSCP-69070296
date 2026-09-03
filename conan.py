"""สมองเป็นเด็กแต่ตัวเป็นผู้ใหญ่"""
word = input()
k = int(input())

k %= 26
ans = ''

for i in word:
    new = chr((ord(i)-ord('a')+ k)% 26 + ord('a'))
    ans += new

print(ans)
