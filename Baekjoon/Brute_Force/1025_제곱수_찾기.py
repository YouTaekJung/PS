n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
res = set()

def bf(cur, x, y, dx, dy):
    temp = int(cur) ** 0.5
    if int(temp) == temp:
        res.add(int(cur))
    x += dx
    y += dy
    if 0 <= x < n and 0 <= y < m:
        cur += matrix[x][y]
        bf(cur, x, y, dx, dy)

if n == 1 and m == 1:
    temp = int(matrix[0][0]) ** 0.5
    print(matrix[0][0] if int(temp) == temp else -1)
else:
    for i in range(n):
        for j in range(m):
            for dx in range(n):
                for dy in range(m):
                    if dx != 0 or dy != 0:
                        bf(matrix[i][j], i, j, dx, dy)
                        bf(matrix[i][j], i, j, -dx, dy)
                        bf(matrix[i][j], i, j, dx, -dy)
                        bf(matrix[i][j], i, j, -dx, -dy)
    print(max(res) if len(res) else -1)