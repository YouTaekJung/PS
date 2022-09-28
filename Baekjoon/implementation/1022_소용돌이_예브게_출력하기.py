r1, c1, r2, c2 = map(int, input().split())
m, d, count = max(abs(r1), abs(c1), abs(r2), abs(c2)), 0, 0
nx = ny = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

count, cur = 0, [0, 0]
board[-c1][-r1] = 1
for v in range(2, (2 * m + 1) ** 2 + 1):
    nx += dx[d]
    ny += dy[d]
    print(nx, ny)
    if 0 <= nx <= c2 - c1 + 1 and 0 <= ny <= r2 - r1 + 1:
        board[nx - c1][ny - r1] = v
    count += 1
    if count == cur[0]:
        cur[1] += 1
        count = 0
        d = d + 1 if d < 3 else 0
    if cur[1] == 2:
        cur = [cur[0] + 1, 0]

for b in board:
    print(*b)