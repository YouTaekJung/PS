import sys
import heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    cur = int(sys.stdin.readline())
    if cur == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(cur), cur))