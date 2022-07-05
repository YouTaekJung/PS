from collections import deque
import sys
input = sys.stdin.readline

def topological_sort():
    dp = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        cur = q.popleft()

        for g in graph[cur]:
            indegree[g] -= 1
            dp[g] = max(dp[g], dp[cur] + cost[g])
            if indegree[g] == 0:
                q.append(g)
            if indegree[last] == 0:
                print(dp[last])
                return

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    cost = [0] +list(map(int, input().split()))
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    last = int(input())
    topological_sort()