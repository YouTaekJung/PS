from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
check[1] = 1

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for n in graph[v]:
            if check[n] == 0:
                check[n] = check[v] + 1
                q.append(n)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
res = sum([1 for t in check if 2 <= t <= 3])
print(res)