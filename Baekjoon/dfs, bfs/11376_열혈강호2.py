import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split()))[1:] for _ in range(n)]
selected = [-1] * (m + 1)

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            return True
    return False

for _ in range(2):
    for i in range(n):
        visited = [0] * n
        bimatch(i)

print(m - selected.count(-1) + 1)