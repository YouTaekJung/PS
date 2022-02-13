n = int(input())
dp = [0, 0, 1, 1] + [1000001] * (n - 3)

for i in range(4, n + 1):
    check = [dp[i-1] + 1]
    if i // 2 == i / 2:
        check.append(dp[i // 2] + 1)
    if i // 3 == i / 3:
        check.append(dp[i // 3] + 1)
    dp[i] = min(check)

print(dp[n])