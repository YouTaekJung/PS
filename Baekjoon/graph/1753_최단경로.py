import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v + 1)]
distance = [200000] * (v + 1)

for _ in range(e):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] >= dist:
            for i in graph[cur]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print('\n'.join(list(map(str, distance[1:]))).replace('200000', 'INF'))