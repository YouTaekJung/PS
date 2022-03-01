n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    l = len(triangle[i])
    for j in range(l):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + triangle[i][j]
        elif j == l - 1:
            dp[i][j] = dp[i - 1][l - 2] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

print(max(dp[-1]))
