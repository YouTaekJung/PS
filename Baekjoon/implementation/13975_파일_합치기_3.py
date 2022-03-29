import heapq
t = int(input())

for _ in range(t):
    k = int(input())
    ans = 0
    li = list(map(int, input().split()))
    h = []
    for l in li:
        heapq.heappush(h, l)
    while len(h) > 1:
        cur = heapq.heappop(h) + heapq.heappop(h)
        ans += cur
        heapq.heappush(h, cur)
    print(ans)