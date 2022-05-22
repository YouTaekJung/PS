n, m, r = map(int, input().split())
INF = int(1e9)
item = [0] + list(map(int, input().split()))
graph = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = c


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = graph[b][a] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for g in graph:
    temp = 0
    for i, l in enumerate(g):
        if l <= m:
            temp += item[i]
    ans = max(temp, ans)

print(ans)