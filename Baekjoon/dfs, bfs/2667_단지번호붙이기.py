import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
matrix = []
res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

for _ in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline()[:-1]))))

def dfs(i, j):
    global count
    count += 1
    matrix[i][j] = 0
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < n and 0 <= y < n and matrix[x][y] == 1:
            matrix[x][y] = 0
            dfs(x, y)
    return count

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            count = 0
            res.append(dfs(i, j))

res.sort()
print(len(res))
for r in res:
    print(r)
