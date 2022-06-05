n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e6)] * 3 for _ in range(n)]
ans = int(1e6)

for i in range(3):
    dp[0] = [int(1e6)] * 3
    dp[0][i] = board[0][i]
    for j in range(1, n):
        dp[j][0] = board[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = board[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = board[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])

print(ans)