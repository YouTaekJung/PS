from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = []
zero, virus = [], []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for i in range(n):
    cur = list(map(int, input().split()))
    for j in range(m):
        if cur[j] == 0:
            zero.append([i, j])
        elif cur[j] == 2:
            virus.append([i, j])
    board.append(cur)

def bfs(b, co):
    global ans

    for c in co:
        b[c[0]][c[1]] = 1

    q = deque([v[:] for v in virus])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not b[nx][ny]:
                b[nx][ny] = 2
                q.append([nx, ny])

    ans = max(ans, sum(b, []).count(0))


com = list(combinations(zero, 3))
for c in com:
    bfs([b[:] for b in board], c)

print(ans)