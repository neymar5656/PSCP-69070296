"""adwefwwve"""
intime = input()
outtime = input()

in_h, in_m = intime.split('.')
out_h, out_m = outtime.split('.')
in_h, in_m = int(in_h), int(in_m)
out_h, out_m = int(out_h), int(out_m)

if not (0 <= in_h <= 23 and 0 <= out_h <= 23 and 0 <= in_m <= 59 and 0 <= out_m <= 59):
    print("ERROR")
else:
    intime_min = (in_h * 60) + in_m
    outtime_min = (out_h * 60) + out_m
    result = outtime_min - intime_min

    if result <= 0 or result > 1440:
        print("ERROR")
    elif result <= 15:
        print("FREE")
    elif result <= 60:
        print(25)
    elif result <= 120:
        print(50)
    elif result <= 180:
        print(80)
    elif result <= 240:
        print(110)
    elif result <= 300:
        print(145)
    elif result <= 360:
        print(180)
    elif result <= 1440:
        print(250)
