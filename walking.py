"""adsasdascfaccadv"""
x = 0
y = 0
text = input()
for i in text:
    if i == 'N':
        y += 1
    elif i == 'S':
        y -= 1
    elif i == 'E':
        x += 1
    elif i == 'W':
        x -= 1
    
print(f"{x} {y} {abs(x) + abs(y)}")
