from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque([[x, y]])
    li = [[x, y]]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(board[x][y] - board[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    li.append([nx, ny])
    return li

ans = 0
while True:
    visited = [[0] * n for _ in range(n)]
    temp = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                temp.append(bfs(i, j))
    if len(temp) == n ** 2:
        print(ans)
        break
    else:
        for tmp in temp:
            s = sum(map(lambda x: board[x[0]][x[1]], tmp))
            for t in tmp:
                board[t[0]][t[1]] = s // len(tmp)
        ans += 1