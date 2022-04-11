from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
check = [[0] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
ans = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append([i, j, 0])

while q:
    x, y, count = q.popleft()
    ans = max(ans, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] == 0 and check[nx][ny] == 0:
                q.append([nx, ny, count + 1])
                board[nx][ny] = 1

flag = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 1
            break
print(-1 if flag else ans)