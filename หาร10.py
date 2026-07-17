'''dsadaaa'''
num = int(input())
num = num//10
text = ""
for i in range(num,-1,-1) :
    text += str(i*10)
    text += " "
text = text.strip()
print(text)
