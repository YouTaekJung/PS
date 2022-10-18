n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + \
                           board[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

def acc(mat, x1, y1, x2, y2):
    return mat[x2][y2] - mat[x1 - 1][y2] - mat[x2][y1 - 1] + mat[x1 - 1][y1 - 1]

ans = -40000
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                ans = max(ans, acc(prefix_sum, x1, y1, x2, y2))

print(ans)