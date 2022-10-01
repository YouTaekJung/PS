from collections import deque

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
visited[0][0] = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque([[0, 0, 0]])
while q:
    x, y, c = q.popleft()
    if x == m - 1 and y == n - 1:
        print(c)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            if board[nx][ny] == 1:
                q.append([nx, ny, c + 1])
            else:
                q.appendleft([nx, ny, c])
