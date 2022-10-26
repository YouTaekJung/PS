from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m):
    li = list(map(int, input().split()))[1:]
    for i in range(len(li) - 1):
        a, b = li[i], li[i + 1]
        graph[a].append(b)
        indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for g in graph[cur]:
        indegree[g] -= 1
        if not indegree[g]:
            q.append(g)
if len(ans) != n:
    print(0)
else:
    for a in ans:
        print(a)