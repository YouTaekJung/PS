n = int(input())

dp = [0] * 1000001
for i in range(2, 1001):
    dp[i * i] = dp[(i - 1) * (i - 1)] + (i - 1) * (i - 1)

idx, plus = 0, 2
for i in range(5, 1000001):
    if not dp[i]:
        plus = int(i ** 0.5)
        idx = 0
    elif idx == plus:
        dp[i] = dp[i - 1]
        idx = 1
    else:
        dp[i] = dp[i - 1] + idx
        idx += 1

print(dp[n:n + 5])
