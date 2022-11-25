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

n, m = int(input()), int(input())
board = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
check_board = [[0] * n for _ in range(n)]

count = 0
for i in range(n):
    count += 1
    check = 0
    for j in range(n - i):
        if board[i + j][j] == 0:
            check_board[i + j][j] = count
            check = 1
        elif board[i + j][j] == 1 and check:
            count += 1
            check = 0
for i in range(1, n):
    count += 1
    check = 0
    for j in range(n - i):
        if board[j][i + j] == 0:
            check_board[j][i + j] = count
            check = 1
        elif board[j][i + j] == 1 and check:
            count += 1
            check = 0
l = count + 1
graph = [[] for _ in range(l)]
count = 0
for i in range(n):
    count += 1
    check = 0
    for j in range(i + 1):
        if board[j][i - j] == 0:
            graph[check_board[j][i - j]].append(count)
            check = 1
        elif board[j][i - j] == 1 and check:
            count += 1
            check = 0

for i in range(1, n):
    count += 1
    check = 0
    for j in range(n - i):
        if board[i + j][n - j - 1] == 0:
            graph[check_board[i + j][n - j - 1]].append(count)
            check = 1
        elif board[i + j][n - j - 1] == 1 and check:
            count += 1
            check = 0
graph += [[] for _ in range(max(0, count))]
l = len(graph)
selected = [-1] * (l)
ans = 0
for i in range(l):
    visited = [0] * l
    if bimatch(i):
        ans += 1
print(ans)

