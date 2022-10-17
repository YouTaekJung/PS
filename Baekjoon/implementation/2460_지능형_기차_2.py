cur, ans = 0, 0
for _ in range(10):
    a, b = map(int, input().split())
    cur += b - a
    cur = max(0, cur)
    ans = max(ans, cur)
print(ans)