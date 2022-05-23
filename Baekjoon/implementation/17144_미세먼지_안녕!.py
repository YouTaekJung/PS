r, c, t = list(map(int, input().split()))
board = []
cleaner = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    cur = list(map(int, input().split()))
    for j in range(c):
        if cur[j] == -1:
            cleaner.append([i, j])
    board.append(cur)

def diffusion(b):
    res = [[0] * c for _ in range(r)]
    [x1, y1], [x2, y2] = cleaner
    res[x1][y1] = res[x2][y2] = -1
    for x in range(r):
        for y in range(c):
            if b[x][y] > 0:
                temp = []
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and res[nx][ny] != -1:
                        temp.append([nx, ny])
                v = b[x][y] // 5
                for t in temp:
                    res[t[0]][t[1]] += v
                res[x][y] += b[x][y] - len(temp) * v
    return res

def moveup(b):
    x1, y1 = cleaner[0]
    prev, cur = 0, 0
    x, y = x1, y1 + 1
    nx, ny = 0, 1
    while [x, y] != [x1, y1]:
        cur = b[x][y]
        b[x][y] = prev
        prev = cur
        x += nx
        y += ny
        if x == x1 and y == c - 1:
            nx, ny = -1, 0
        elif x == 0 and y == c - 1:
            nx, ny = 0, -1
        elif x == 0 and y == 0:
            nx, ny = 1, 0

def movedown(b):
    x2, y2 = cleaner[1]
    prev, cur = 0, 0
    x, y = x2, y2 + 1
    nx, ny = 0, 1
    while [x, y] != [x2, y2]:
        cur = b[x][y]
        b[x][y] = prev
        prev = cur
        x += nx
        y += ny
        if x == x2 and y == c - 1:
            nx, ny = 1, 0
        elif x == r - 1 and y == c - 1:
            nx, ny = 0, -1
        elif x == r - 1 and y == 0:
            nx, ny = -1, 0

for _ in range(t):
    board = diffusion(board)
    moveup(board)
    movedown(board)

print(sum(sum(board, [])) + 2)