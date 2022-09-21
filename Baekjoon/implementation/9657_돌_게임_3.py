n = int(input())
dp = [0] * 1001
dp[1] = dp[3] = dp[4] = 1

for i in range(5, n + 1):
    if not min(dp[i - 1], dp[i - 3], dp[i - 4]):
        dp[i] = 1

print('SK' if dp[n] else 'CY')