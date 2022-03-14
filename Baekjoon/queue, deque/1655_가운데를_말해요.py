import sys
import heapq

n = int(sys.stdin.readline())
max_h = [-int(sys.stdin.readline())]
min_h = []
check = -max_h[0]
print(check)

for i in range(1, n):
    cur = int(sys.stdin.readline())
    if cur > check:
        heapq.heappush(min_h, cur)
    else:
        heapq.heappush(max_h, -cur)

    if i % 2 == 1:
        while len(max_h) != len(min_h):
            if len(max_h) > len(min_h):
                heapq.heappush(min_h, -heapq.heappop(max_h))
            else:
                heapq.heappush(max_h, -heapq.heappop(min_h))
        check = -max_h[0]
        print(min(-max_h[0], min_h[0]))
    else:
        while len(max_h) - 1 != len(min_h):
            if len(max_h) - 1 > len(min_h):
                heapq.heappush(min_h, -heapq.heappop(max_h))
            else:
                heapq.heappush(max_h, -heapq.heappop(min_h))
        check = -max_h[0]
        print(check)