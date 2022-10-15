from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topological_sort():
    ans = []
    h = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(h, i)

    while h:
        cur = heappop(h)
        ans.append(cur)

        for g in graph[cur]:
            indegree[g] -= 1
            if indegree[g] == 0:
                heappush(h, g)
    print(*ans)

topological_sort()
