from collections import deque

n = int(input())
board, start = [], []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
size, fish, count = 2, 0, 0
ans = 0

for i in range(n):
    li = list(map(int, input().split()))
    for j, l in enumerate(li):
        if l == 9:
            li[j] = 0
            start = [i, j]
        elif l > 0:
            fish += 1
    board.append(li)

def bfs(x, y):
    global size, fish, count, ans
    visited = [[0] * n for _ in range(n)]
    li = []
    m = 10 ** 6
    q = deque([[x, y, 0]])
    while q:
        x, y, time = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] in [0, size]:
                    visited[nx][ny] = 1
                    if time + 1 <= m:
                        q.append([nx, ny, time + 1])
                elif 0 < board[nx][ny] < size:
                    visited[nx][ny] = 1
                    li.append([nx, ny, time + 1])
                    m = time + 1
    if len(li):
        nx, ny, time = sorted(li, key=lambda x: (x[2], x[0], x[1]))[0]
        board[nx][ny] = 0
        ans += time
        count += 1
        fish -= 1
        if size == count:
            size += 1
            count = 0
        return [nx, ny]
    return False

while fish:
    start = bfs(start[0], start[1])
    if not start:
        break

print(ans)
