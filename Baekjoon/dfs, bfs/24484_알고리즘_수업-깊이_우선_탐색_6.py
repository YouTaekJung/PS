import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [[-1, 0] for _ in range(n + 1)]
count = 1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    global count

    graph[node].sort(reverse=True)
    for g in graph[node]:
        if visited[g][0] == -1:
            count += 1
            visited[g] = [visited[node][0] + 1, count]
            dfs(g)

visited[r][0] = 0
dfs(r)

ans = 0
for v in visited[1:]:
    ans += v[0] * v[1]
print(ans)
