n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

m, ans = -1, -1
for i in range(n):
    s = set()
    for j in range(5):
        for k in range(n):
            if li[i][j] == li[k][j]:
                s.add(k)

    if len(s) > m:
        ans = i + 1
        m = len(s)

print(ans)