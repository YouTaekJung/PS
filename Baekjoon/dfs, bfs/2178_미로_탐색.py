from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0])
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < n and 0 <= y < m and matrix[x][y] == 1:
                if visited[x][y] == 0 or visited[x][y] > visited[i][j] + 1:
                    q.append([x, y])
                    visited[x][y] = visited[i][j] + 1
    return
bfs()
print(visited[n - 1][m - 1] + 1)

# import sys
# sys.setrecursionlimit(10**6)
#
# n, m = map(int, input().split())
# matrix = [list(map(int, list(input()))) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x,y):
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
#             if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 if nx == n-1 and ny == m - 1:
#                     return
#                 dfs(nx,ny)
#     return
#
# dfs(0,0)
# print(visited[n - 1][m - 1] + 1)
