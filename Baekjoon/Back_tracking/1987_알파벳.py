r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
check = [0] * 26
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1

def dfs(x, y, count):
    global ans
    ans = max(ans, count)

    check[ord(board[x][y]) - 65] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not check[ord(board[nx][ny]) - 65]:
                dfs(nx, ny, count + 1)
    check[ord(board[x][y]) - 65] = 0

dfs(0, 0, 1)
print(ans)