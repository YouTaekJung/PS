n = int(input())
li = [list(map(float, input().split())) for _ in range(n)]
li.sort(key=lambda x: (x[1], x[0]))
ans = 0

for i in range(n - 1):
    [x1, y1], [x2, y2] = li[i], li[i + 1]
    ans += round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

print(ans)