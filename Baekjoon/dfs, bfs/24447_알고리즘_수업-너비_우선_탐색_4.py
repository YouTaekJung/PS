from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [[-1, 0] for _ in range(n + 1)]
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global count

    q = deque([r])
    visited[r][0] = 0
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for g in graph[v]:
            if visited[g][0] == -1:
                count += 1
                visited[g] = [visited[v][0] + 1, count]
                q.append(g)
bfs(r)

ans = 0
for v in visited:
    ans += v[0] * v[1]
print(ans)