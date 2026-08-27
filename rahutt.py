"""gggg"""
S = input().upper()

password = []

for i in range(10):
    if (i + 1) % 2:
        value = ord(S[0]) + i
    else:
        value = ord(S[-1]) - i

    value = (value % len(S)) % 10
    password.append(value)

for i in range(2, 8):
    print(password[i], end=" ")

print()