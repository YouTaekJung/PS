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

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
selected = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)

ans = 0
for i in range(n):
    visited = [0] * n
    if bimatch(i):
        ans += 1
print(ans)