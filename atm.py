"""fsdafdsezoplbhmjiedrtjg"""
num = int(input())

pun = num//1000
a1 = num%1000
haroy = a1//500
a2 = a1%500
hundred = a2//100

if num % 100 :
    print("ERROR")
else:
    if 100 <= num < 500:
        print(f"100 = {num//100}")
    elif 500 <= num < 1000:
        if num == 500:
            print(f"500 = {num//500}")
        else:
            print(f"500 = {num//500}")
            print(f"100 = {hundred}")
    elif num >=1000:
        if not a1:
            print(f"1000 = {num//1000}")
        else:
            if a1 == 500:
                print(f"1000 = {pun}")
                print(f"500 = {haroy}")
            elif a1 < 500:
                print(f"1000 = {pun}")
                print(f"100 = {hundred}")
            elif a1 >500 and a2 > 0:
                print(f"1000 = {pun}")
                print(f"500 = {haroy}")
                print(f"100 = {hundred}")
