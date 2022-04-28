n, m = map(int, input().split())
ans = []
last = 0

for i in range(n - 1):
    if n - i > m:
        ans.append([i, i + 1])
        last = i + 1
    else:
        ans.append([last, i + 1])

for a in ans:
    print(*a)