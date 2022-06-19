from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
d = [0 for _ in range(n + 1)]
q = deque()
ans = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    d[b] += 1

for i in range(1, n + 1):
    if d[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    ans.append(cur)
    for g in graph[cur]:
        d[g] -= 1
        if d[g] == 0:
            q.append(g)

print(*ans)