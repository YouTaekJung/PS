from collections import deque
n = int(input())
v = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
check = [0] * (n+1)

for _ in range(v):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

def bfs(v):
    res = 0
    queue = deque()
    queue.append(v)
    check[v] = 1

    while queue:
        v = queue.popleft()
        res += 1
        for i in range(1, n+1):
            if matrix[v][i] == 1 and check[i] == 0:
                queue.append(i)
                check[i] = 1
    return res
print(bfs(v))