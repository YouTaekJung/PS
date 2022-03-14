import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    count = 0
    li = []
    while count <= (n - 1) // 10:
        li += list(map(int, sys.stdin.readline().split()))
        count += 1
    max_h = [-li[0]]
    min_h = []
    check = -max_h[0]
    res = [check]

    for i in range(1, len(li)):
        cur = li[i]
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
        else:
            while len(max_h) - 1 != len(min_h):
                if len(max_h) - 1 > len(min_h):
                    heapq.heappush(min_h, -heapq.heappop(max_h))
                else:
                    heapq.heappush(max_h, -heapq.heappop(min_h))
            check = -max_h[0]
            res.append(check)
    print(len(res))
    count = 0
    while count <= (len(res) - 1) // 10:
        print(*res[count * 10:min((count + 1) * 10, n)])
        count += 1