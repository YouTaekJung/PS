from collections import deque

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = [0, 0]

def bfs(x, y):
    q = deque([[i, j]])
    start = matrix[i][j]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == start and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            ans[0] += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            ans[1] += 1
            bfs(i, j)
print(*ans)