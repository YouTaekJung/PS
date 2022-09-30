from collections import deque
n, m = map(int, input().split())

board = [list(map(lambda x: [x, 0], list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy, d = [-1, 1, 0, 0], [0, 0, -1, 1], 1

q = deque([[0, 0]])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[x][y][0] == 'A':

            elif board[x][y][0] == 'C':

            elif board[x][y][0] == 'D':
