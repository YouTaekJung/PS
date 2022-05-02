n, k = map(int, input().split())
dp = [[] for _ in range(n + 1)]
dp[1] = [1]

for i in range(2, n + 1):
    dp[i].append(i)
    for j in range(1, i - 1):
        dp[i].append((dp[i - 1][j - 1] + dp[i - 1][j]) % 10007)
    dp[i].append(1)

print(dp[n][k - 1])
