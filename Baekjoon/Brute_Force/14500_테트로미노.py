from itertools import combinations

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        if i < n - 3:
            res = max(res, sum([mat[i + k][j] for k in range(4)]))
        if j < m - 3:
            res = max(res, sum(mat[i][j:j + 4]))
        if i < n - 1 and j < m - 2:
            minus = 2000
            com = list(combinations([[i, j], [i, j + 1], [i, j + 2],
                                     [i + 1, j], [i + 1, j + 1], [i + 1, j + 2]], 2))
            for c in com:
                [x1, y1], [x2, y2] = c
                if not ((abs(y1 - y2) == 1 or y1 == y2 == j + 1) and abs(x1 - x2) == 1):
                    minus = min(minus, mat[x1][y1] + mat[x2][y2])
            res = max(res, sum(mat[i][j:j + 3]) + sum(mat[i + 1][j:j + 3]) - minus)
        if i < n - 2 and j < m - 1:
            minus = 2000
            com = list(combinations([[i, j], [i + 1, j], [i + 2, j],
                                     [i, j + 1], [i + 1, j + 1], [i + 2, j + 1]], 2))
            for c in com:
                [x1, y1], [x2, y2] = c
                if not ((abs(x1 - x2) == 1 or x1 == x2 == i + 1) and abs(y1 - y2) == 1):
                    minus = min(minus, mat[x1][y1] + mat[x2][y2])

            res = max(res, sum([sum(mat[i + k][j:j + 2]) for k in range(3)]) - minus)
print(res)