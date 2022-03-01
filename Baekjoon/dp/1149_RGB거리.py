n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = color[0]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 2]) + color[i][j]

print(min(dp[-1]))