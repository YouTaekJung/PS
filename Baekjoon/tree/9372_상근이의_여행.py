import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

t = int(input())

def dfs(node, c):
    visited[node] = 1
    for g in graph[node]:
        if visited[g] == 0:
            c = dfs(g, c + 1)
    return c

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    visited[1] = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    count = dfs(1, 0)
    print(count)