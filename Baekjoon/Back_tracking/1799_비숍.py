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

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
check_board = [[0] * n for _ in range(n)]

count = 0
for i in range(n):
    count += 1
    for j in range(n - i):
        if board[i + j][j] == 1:
            check_board[i + j][j] = count

for i in range(1, n):
    count += 1
    for j in range(n - i):
        if board[j][i + j] == 1:
            check_board[j][i + j] = count

l = count + 1
graph = [[] for _ in range(l)]
count = 0
for i in range(n):
    count += 1
    for j in range(i + 1):
        if board[j][i - j] == 1:
            graph[check_board[j][i - j]].append(count)

for i in range(1, n):
    count += 1
    for j in range(n - i):
        if board[i + j][n - j - 1] == 1:
            graph[check_board[i + j][n - j - 1]].append(count)
            check = 1
graph += [[] for _ in range(max(0, count))]
l = len(graph)
selected = [-1] * (l)
ans = 0
for i in range(l):
    visited = [0] * l
    if bimatch(i):
        ans += 1
print(ans)

