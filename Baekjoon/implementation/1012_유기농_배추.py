import sys
sys.setrecursionlimit(10**6)

def check(i, j):
    li = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    for l in li:
        if 0 <= l[0] < m and 0 <= l[1] < n and matrix[l[1]][l[0]] == 1:
            matrix[l[1]][l[0]] = 0
            check(l[0], l[1])
    return

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    res = 0
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    for i in range(m):
        for j in range(n):
            if matrix[j][i] == 1:
                res += 1
                check(i, j)
    print(res)