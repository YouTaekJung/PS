import heapq

n = int(input())
min_h, max_h = [], []
ans = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        heapq.heappush(max_h, -num)
    elif num == 1:
        ans += 1
    else:
        heapq.heappush(min_h, num)

while len(min_h) > 1:
    x, y = heapq.heappop(min_h), heapq.heappop(min_h)
    ans += x * y

while len(max_h) > 1:
    x, y = heapq.heappop(max_h), heapq.heappop(max_h)
    ans += x * y

print(ans + sum(min_h) - sum(max_h))