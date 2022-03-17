from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1
    while q:
        node = q.popleft()
        for g in graph[node]:
            if check[g] == 0:
                check[g] = check[node] + 1
                q.append(g)

bfs(1)
m = max(check)
print(check.index(m), m - 1, check.count(m))