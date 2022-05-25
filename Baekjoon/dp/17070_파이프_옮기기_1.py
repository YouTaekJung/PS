n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if board[i][j - 1] != 1:
            dp[i][j][0] += dp[i][j - 1][0]
            if i > 0:
                dp[i][j][0] += dp[i][j - 1][2]
        if board[i - 1][j] != 1:
            dp[i][j][1] += dp[i - 1][j][1]
            if i > 0:
                dp[i][j][1] += dp[i - 1][j][2]
        if i > 0 and not board[i][j - 1] + board[i - 1][j] + board[i - 1][j - 1]:
            dp[i][j][2] += sum(dp[i - 1][j - 1])
print(sum(dp[-1][-1]) if board[-1][-1] != 1 else 0)