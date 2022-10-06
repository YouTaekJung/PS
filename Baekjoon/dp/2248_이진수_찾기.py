n, l, i = map(int, input().split())
dp = [[0] * 32 for _ in range(32)]

for i in range(31):
    dp[0][i] = 1
for i in range(1, 32):
    dp[i][0] = dp[i - 1][0]
    for j in range(1, 32):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

for i in range(n, 0, -1):
    if i <= dp[i - 1][l]:
        print('0', end="")
    else:
        print('1', end="")
        i -= dp[i - 1][l]
        l -= 1