v, e = map(int, input().split())
graph = [[0] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    x, y, k = map(int, input().split())
    graph[x][y] = graph[y][x] = k

def dijkstra