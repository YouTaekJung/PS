from collections import deque
n = int(input())
m = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

def bfs(v):
    res = 0
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        p = queue.popleft()
        res += 1
        for i in range(1, n + 1):
            if matrix[i][p] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return res

print(bfs(1) - 1)

