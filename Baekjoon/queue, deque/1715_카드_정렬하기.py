import sys
import heapq

n = int(sys.stdin.readline())
h = []
res = 0
for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

while len(h) > 1:
    cur = heapq.heappop(h) + heapq.heappop(h)
    res += cur
    heapq.heappush(h, cur)

print(res)