"""dsasdwdqqwe"""
s = input().strip()
n = len(s)
s_upper = s.upper()

max_u = 0

for i in range(n):
    if s_upper[i] == 'B':
        u_count = 0
        j = i + 1

        while j < n and s_upper[j] == 'U':
            u_count += 1
            j += 1

        if u_count >= 2 and u_count > max_u:
            max_u = u_count

if max_u >= 2:
    print("Yes", max_u)

else:
    first_b = -1

    for i in range(n):
        if s_upper[i] == 'B':
            first_b = i
            break

    if first_b != -1:
        result = s[:first_b + 1] + "U" * (n - first_b - 1)
        print(result)

    else:
        P = "BUU"
        result = ""

        for i in range(n):
            result += P[i % 3]

        print(result)
