import heapq

n = int(input())
h = []
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range(n):
        if len(h) < n:
            heapq.heappush(h, temp[i])
        else:
            if h[0] < temp[i]:
                heapq.heappop(h)
                heapq.heappush(h, temp[i])

print(h[0])