"""songkram"""
place1 ,place2 = input().split()
weight = float(input())
price = 0

if place1 == "BKK":
    if place2 == "CNX":
        price = 10+(30*weight)
    elif place2 == 'PKT':
        price = 25+(50*weight)
    else:
        price = "Error"
elif place1 == "UBP":
    if place2 == "BKK":
        price = 20+(40*weight)
    elif place2 == "PKT":
        price = 40+(70*weight)
    else:
        price = "Error"
elif place1 == "CNX" and place2 == "UBP":
    price = 15+(40*weight)
elif place1 == "PKT" and place2 == "CNX":
    price = 30+(60*weight)
else:
    price = "Error"

if price == "Error":
    print("Error")
else:
    price = float(price)
    print(f"{price:.2f}")
