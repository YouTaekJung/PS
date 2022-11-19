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
board = [list(input()) for _ in range(n)]
row_board = [[0] * n for _ in range(n)]

count = 0
for i in range(n):
    count += 1
    for j in range(n):
        if board[i][j] == '.':
            row_board[i][j] = count
        else:
            count += 1

l = count + 1
graph = [[] for _ in range(l)]
count = 0
for i in range(n):
    count += 1
    check = 0
    for j in range(n):
        if board[j][i] == '.':
            graph[row_board[j][i]].append(count)
        else:
            count += 1

graph += [[] for _ in range(max(0, count))]
l = len(graph)
selected = [-1] * (l)
ans = 0
for i in range(l):
    visited = [0] * l
    if bimatch(i):
        ans += 1
print(ans)

