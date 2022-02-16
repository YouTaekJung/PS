s = list(map(int, list(input())))
count = [0, 0]
count[s[0]] += 1
prev = s[0]

for i in range(1, len(s)):
    if prev != s[i]:
        count[s[i]] += 1
        prev = s[i]

print(min(count))