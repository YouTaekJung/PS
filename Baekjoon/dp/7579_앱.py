n, m = map(int, input().split())
li = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(n + 1)]
ans = 1e7 * n

for i in range(n):
    for j in range(sum(cost)):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], li[i] + dp[i - 1][j - cost[i]])
        if dp[i][j] >= m:
            ans = min(ans, j)

if n == 1:
    print(cost[0])
elif ans == 1e7 * n:
    print(n * m)
else:
    print(ans)
