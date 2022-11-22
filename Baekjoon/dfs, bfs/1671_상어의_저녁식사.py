import sys
input = sys.stdin.readline

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for i in range(n):
        if graph[num][i]:
            if selected[i] == -1 or bimatch(selected[i]):
                selected[i] = num
                return True
    return False

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
graph = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            if li[i][0] == li[j][0] and li[i][1] == li[j][1] and li[i][2] == li[j][2] and i > j:
                continue
            if li[i][0] >= li[j][0] and li[i][1] >= li[j][1] and li[i][2] >= li[j][2]:
                graph[i][j] = 1

selected = [-1] * n
ans = 0
for _ in range(2):
    for i in range(n):
        visited = [0] * n
        if bimatch(i):
            ans += 1
print(n - ans)