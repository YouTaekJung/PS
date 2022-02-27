import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visit = [0 for i in range(n + 1)]
count = 0

def dfs(i):
    visit[i] = 1
    for j in range(1, n + 1):
        if matrix[i][j] == 1 and visit[j] == 0:
            dfs(j)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        count += 1
print(count)