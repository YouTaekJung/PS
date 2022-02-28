from collections import deque

r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
res = [0, 0]

def bfs(i, j):
    global w, s
    visited[i][j] = 1
    q.append([i, j])
    while q:
        x, y = q.popleft()
        if matrix[x][y] == 'v':
            w += 1
        elif matrix[x][y] == 'o':
            s += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] != '#' and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1


for i in range(r):
    for j in range(c):
        if matrix[i][j] != '#' and visited[i][j] == 0:
            w, s = 0, 0
            bfs(i, j)
            if w >= s:
                res[1] += w
            else:
                res[0] += s


print(*res)