from collections import deque

n, m, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
check = [[[0] * n for _ in range(m)] for _ in range(h)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 0, 1]
q = deque()
ans = 0

for i in range(m):
    for j in range(n):
        for k in range(h):
            if board[k][i][j] == 1:
                q.append([i, j, k, 0])

while q:
    x, y, z, count = q.popleft()
    ans = max(ans, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[z][nx][ny] == 0 and check[z][nx][ny] == 0:
                q.append([nx, ny, z, count + 1])
                board[z][nx][ny] = 1
    for i in range(3):
        nz = z + dz[i]
        if 0 <= nz < h:
            if board[nz][x][y] == 0 and check[nz][x][y] == 0:
                q.append([x, y, nz, count + 1])
                board[nz][x][y] = 1

flag = 0
for i in range(m):
    for j in range(n):
        for k in range(h):
            if board[k][i][j] == 0:
                flag = 1
                break
print(-1 if flag else ans)