"""sdasfcdavgqwAEGB"""
card = input()
t = ''
pos = ''
if card[-1] == 'D':
    t = "of diamonds"
elif card[-1] == 'H':
    t = "of hearts"
elif card[-1] == 'S':
    t = "of spades"
elif card[-1] == 'C':
    t = "of clubs"

if len(card) > 2:
    pos = '10 '
else:
    if card[0] == 'Q':
        pos = 'queen '
    elif card[0] == 'A':
        pos = 'ace '
    elif card[0] == 'K':
        pos = 'king '
    elif card[0] == 'J':
        pos = 'jack '
    elif card[0] == '1':
        pos = '1 '
    elif card[0] == '2':
        pos = '2 '
    elif card[0] == '3':
        pos = '3 '
    elif card[0] == '4':
        pos = '4 '
    elif card[0] == '5':
        pos = '5 '
    elif card[0] == '6':
        pos = '6 '
    elif card[0] == '7':
        pos = '7 '
    elif card[0] == '8':
        pos = '8 '
    elif card[0] == '9':
        pos = '9 '

print(pos + t)
