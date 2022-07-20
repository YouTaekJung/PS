import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
graph = [[[INF, [i, j]] for j in range(n + 1)] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b][0] = min(graph[a][b][0], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if graph[i][j][0] > graph[i][k][0] + graph[k][j][0]:
                    graph[i][j][0] = graph[i][k][0] + graph[k][j][0]
                    graph[i][j][1] = graph[i][k][1] + graph[k][j][1][1:]
            else:
                graph[i][j][0] = 0

for g in graph[1:]:
    print(' '.join(list(map(lambda x: str(x[0]), g[1:]))))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j][0] == 0:
            print(0)
        else:
            print(len(graph[i][j][1]), *graph[i][j][1])
