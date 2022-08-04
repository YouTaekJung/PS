from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global count

    q = deque([r])
    visited[r] = 0
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == -1:
                visited[g] = visited[v] + 1
                q.append(g)
bfs(r)

for v in visited[1:]:
    print(v)