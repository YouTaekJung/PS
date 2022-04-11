n = int(input())
INF = int(1e9)
graph = [list(map(lambda x: 1 if x == '1' else INF, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        graph[i][j] = 0 if graph[i][j] == INF else 1

for g in graph:
    print(*g)