"""promotion"""
pen,book,case = input().split()
piece = int(pen) + int(book) + int(case)

pen = 25*int(pen)
book = 40*int(book)
case = 55*int(case)

total = pen + book + case

if piece >=3:
    total = total * 0.9

print(int(total))
