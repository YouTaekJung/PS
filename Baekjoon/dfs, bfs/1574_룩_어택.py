import sys
input = sys.stdin.readline

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            return True
    return False

r, c, n = map(int, input().split())
board = [[0] * (c) for _ in range(r)]
for _ in range(n):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

row_board = [[0] * c for _ in range(r)]

count = 0
for i in range(r):
    count += 1
    check = 0
    for j in range(c):
        if not board[i][j]:
            row_board[i][j] = count

l = count + 1
graph = [[] for _ in range(l)]
count = 0
for i in range(c):
    count += 1
    check = 0
    for j in range(r):
        if not board[j][i]:
            graph[row_board[j][i]].append(count)

graph += [[] for _ in range(max(0, count))]
l = len(graph)
selected = [-1] * (l)
ans = 0
for i in range(l):
    visited = [0] * l
    if bimatch(i):
        ans += 1
print(ans)

