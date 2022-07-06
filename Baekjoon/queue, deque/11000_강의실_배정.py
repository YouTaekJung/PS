from heapq import heappush, heappop

n = int(input())
q = sorted([list(map(int, input().split())) for _ in range(n)])
h = []
heappush(h, q[0][1] )

for i in range(1, n):
    if q[i][0] < h[0]:
        heappush(h, q[i][1])
    else:
        heappop(h)
        heappush(h, q[i][1])

print(len(h))
