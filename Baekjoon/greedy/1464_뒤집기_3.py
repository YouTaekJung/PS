s = input()

for i in range(len(s) - 1):
    if s[i] > s[i + 1] and s[i + 1] <= s[0]:
        s = s[:i + 1][::-1] + s[i + 1:]
        if s[i] >= s[i + 1]:
            s = s[:i + 2][::-1] + s[i + 2:]

print(s)