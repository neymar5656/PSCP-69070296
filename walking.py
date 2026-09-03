"""adsasdascfaccadv"""
x = 0
y = 0
text = input()
text = list(text)
for _ in range(len(text)):

    if 'N' in text:
        y +=1 
    elif 'S' in text:
        y -= 1
    elif 'E' in text:
        x += 1
    elif 'W' in text:
        x -= 1
    del text[0]
    
print(f"{x} {y} {abs(x) + abs(y)}")
