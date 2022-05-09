import sys
input = sys.stdin.readline
tc = int(input())

def bellmanford(start):
    dist[start] = 0
    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    dist = [10000] * (n + 1)
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print('YES' if bellmanford(1) else 'NO')
