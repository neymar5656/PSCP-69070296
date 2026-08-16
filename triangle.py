"""I LOVE MY JOB"""
def main():
    """I LOVE YOUNGGU"""
    a = int(input())
    i = 1
    for i in range(a):
        if i in range(1,3):
            print("0" * i)
        elif 2 < i < a:
            print(f"0{'1' * (i - 2)}0")
    print("0" * a)
main()
