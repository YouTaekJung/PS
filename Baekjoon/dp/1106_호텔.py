c, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0] + [1e9] * (c + 100)

for x, y in li:
    for i in range(y, c + 101):
        dp[i] = min(dp[i], dp[i - y] + x)

print(min(dp[c:c + 101]))