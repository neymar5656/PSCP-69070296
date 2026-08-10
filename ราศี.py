"""rasee"""
day = int(input())
mon = int(input())

if mon == 12 and day >= 22 or mon == 1 and day <= 19:
    print("capricorn")
elif mon == 1 and day >= 20 or mon == 2 and day <= 18:
    print("aquarius")
elif mon == 2 and day >= 19 or mon == 3 and day <= 20:
    print("pisces")
elif mon == 3 and day >= 21 or mon == 4 and day <= 19:
    print("aries")
elif mon == 4 and day >= 20 or mon == 5 and day <= 20:
    print("taurus")
elif mon == 5 and day >= 21 or mon == 6 and day <= 21:
    print("gemini")
elif mon == 6 and day >= 22 or mon == 7 and day <= 12:
    print("cancer")
elif mon == 7 and day >= 23 or mon == 8 and day <= 22:
    print("leo")
elif mon == 8 and day >= 23 or mon == 9 and day <= 22:
    print("virgo")
elif mon == 9 and day >= 23 or mon == 10 and day <= 23:
    print("libra")
elif mon == 10 and day >= 24 or mon == 11 and day <= 21:
    print("scorpio")
elif mon == 11 and day >= 22 or mon == 12 and day <= 21:
    print("sagittarius")
