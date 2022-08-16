n = int(input())
city = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans, d = 0, 0
prev = cost.pop(0)

for i in range(n - 1):
    d += city[i]
    if prev > cost[i]:
        ans += prev * d
        prev = cost[i]
        d = 0

print(ans + prev * d)