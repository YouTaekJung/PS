from collections import deque

matrix = [list(map(int, input().split())) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
res = []

def bfs(i, j):
    q.append([i, j, []])

    while q:
        x, y, l = q.popleft()
        if len(l) == 6:
            res.append(''.join(map(str, l)))
        else:
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    q.append([nx, ny, l + [matrix[nx][ny]]])

for i in range(5):
    for j in range(5):
        bfs(i, j)

print(len(set(res)))