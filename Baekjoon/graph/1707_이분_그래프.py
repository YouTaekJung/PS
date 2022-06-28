from collections import deque
import sys
input = sys.stdin.readline
k = int(input())

def bfs(node):
    q = deque([node])
    visited[node] = 1
    while q:
        cur = q.popleft()
        for g in graph[cur]:
            if not visited[g]:
                visited[g] = -visited[cur]
                q.append(g)
            elif visited[g] == visited[cur]:
                return False
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v + 1):
        if not visited[i]:
            ans = bfs(i)
            if not ans:
                break
    print('YES' if ans else 'NO')

