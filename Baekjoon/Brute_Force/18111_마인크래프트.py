n, m, b = map(int, input().split())
ground = []
min_h, max_h, ans = 256, 0, [1e15, 256]
for _ in range(n):
    cur = list(map(int, input().split()))
    min_h = min([min_h] + cur)
    max_h = max([max_h] + cur)
    ground.append(cur)

for h in range(min_h, max_h + 1):
    s = 0
    inv = b
    for i in range(n):
        for j in range(m):
            d = h - ground[i][j]
            if d > 0:
                s += d
                inv -= d
            else:
                s -= 2 * d
                inv -= d
    if 0 <= inv:
        if s < ans[0] or (s == ans[0] and h > ans[1]):
            ans = [s, h]
print(*ans)