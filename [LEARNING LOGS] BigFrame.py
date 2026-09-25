"""stupid"""
text = []

for _ in range(5):
    text.append(input())

max_len = max(len(line) for line in text)

print("*" * (max_len + 4))

for line in text:
    print("* " + line.ljust(max_len) + " *")

print("*" * (max_len + 4))
