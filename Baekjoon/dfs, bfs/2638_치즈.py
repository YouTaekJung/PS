from collections import deque

n, m = map(int, input().split())
board, cheeze = [], deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(m):
        if li[j] == 1:
            cheeze.append([i, j])
    board.append(li)

def outer():
    visited = [[0] * m for _ in range(n)]
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        board[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                    not visited[nx][ny] and board[nx][ny] < 1:
                visited[nx][ny] = 1
                q.append([nx, ny])


def disappear():
    count = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                count += 1
                check = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if board[nx][ny] == -1:
                        check += 1
                if check >= 2:
                    board[x][y] = 0
    return 1 if count else 0

ans = 0
while True:
    outer()
    check = disappear()
    if not check:
        break
    ans += 1

print(ans)