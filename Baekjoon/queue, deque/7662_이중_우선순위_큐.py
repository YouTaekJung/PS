import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    min_h = []
    max_h = []
    check = [0] * n
    for i in range(n):
        command = sys.stdin.readline().split()
        if command[0] == 'I':
            heapq.heappush(min_h, (int(command[1]), i))
            heapq.heappush(max_h, (-int(command[1]), i))
            check[i] = 1
        else:
            if command[1] == '1':
                while max_h and not check[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    check[max_h[0][1]] = 0
                    heapq.heappop(max_h)
            else:
                while min_h and not check[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    check[min_h[0][1]] = 0
                    heapq.heappop(min_h)
    while min_h and not check[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not check[max_h[0][1]]:
        heapq.heappop(max_h)

    print(*[-heapq.heappop(max_h)[0], heapq.heappop(min_h)[0]] if len(min_h) else 'EMPTY')