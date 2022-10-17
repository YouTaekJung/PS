n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def sum_board(board):
    s = [[sum(board[i][:j + 1]) for j in range(len(board[0]))]
                for i in range(len(board))]

    for i in range(len(s) - 1):
        for j in range(len(s[0])):
            s[i + 1][j] += s[i][j]

    return s

def acc(mat, x1, y1, x2, y2):
    return mat[x2][y2] - mat[x1][y2] - mat[x2][y1] + mat[x1][y1]

mat, ans = sum_board(board), 0
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                ans = max(ans, acc(mat, x1, y1, x2, y2))

print(ans)