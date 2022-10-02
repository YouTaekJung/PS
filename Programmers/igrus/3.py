n, li = int(input()), list(input())
m, s = int(input()), list(input())
i, j, count = n - 1, 0, 0

for c in set(s):
    if c not in li:
        print(-1)
        exit()

while j < m:
    i += 1
    if i == n:
        i = 0
    count += 1
    if s[j] == li[i]:
        j += 1
print(count)