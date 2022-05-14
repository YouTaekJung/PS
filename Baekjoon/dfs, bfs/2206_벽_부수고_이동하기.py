from collections import deque

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque([[0, 0, 0]])

while q:
    x, y, b = q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][b])
        exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and visited[nx][ny][b] == 0:
                q.append([nx, ny, b])
                visited[nx][ny][b] = visited[x][y][b] + 1
            if board[nx][ny] == 1 and b == 0:
                q.append([nx, ny, 1])
                visited[nx][ny][1] = visited[x][y][0] + 1

print(-1)