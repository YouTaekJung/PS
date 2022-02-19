n, m = map(int, input().split())
li = [[0] * m for _ in range(n)]

for _ in range(2):
    for i in range(n):
        cur = list(map(int, input().split()))
        for j in range(m):
            li[i][j] += cur[j]

for l in li:
    print(*l)