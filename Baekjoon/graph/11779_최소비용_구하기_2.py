import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
path = [[i] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = path[now] + [i[0]]
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])
print(len(path[end]))
print(*path[end])
