from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

def bfs(v):
    q = deque()
    q.append([v, 0])

    while q:
        cur = q.popleft()
        if cur[0] == b:
            return cur[1]
        for i in range(1, n + 1):
            if matrix[cur[0]][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append([i, cur[1] + 1])
    return -1

print(bfs(a))