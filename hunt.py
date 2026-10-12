"""arariraf"""
unit_op, unit_num = input().split()
tens_op, tens_num = input().split()
hundreds_op, hundreds_num = input().split()

unit_num = int(unit_num)
tens_num = int(tens_num)
hundreds_num = int(hundreds_num)

def check(value, op, target):
    """hyuiku"""
    if op == "==":
        result = value == target
    elif op == "!=":
        result = value != target
    elif op == ">":
        result = value > target
    elif op == "<":
        result = value < target
    elif op == ">=":
        result = value >= target
    else:
        result = value <= target
    return result

for num in range(1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    unit = num % 10

    if (check(unit, unit_op, unit_num)
            and check(tens, tens_op, tens_num)
            and check(hundreds, hundreds_op, hundreds_num)):
        print(f"{num:03d}")
