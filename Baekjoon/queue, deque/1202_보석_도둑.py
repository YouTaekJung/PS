import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, k = map(int, sys.stdin.readline().split())
jewelry = sorted([list(map(int, input().split())) for _ in range(n)])
bag = sorted([int(input()) for _ in range(k)])
ans, temp = 0, []

for b in bag:
    while jewelry and b >= jewelry[0][0]:
        heappush(temp, -jewelry[0][1])
        heappop(jewelry)
    if temp:
        ans += heappop(temp)
    elif not jewelry:
        break

print(-ans)