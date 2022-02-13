n = int(input())
dp = [[1, 0], [0, 1]]
li = []
m = 0

for _ in range(n):
    cur = int(input())
    if m < cur:
        m = cur
    li.append(cur)

for i in range(2, m + 1):
    dp.append([dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]])

for num in li:
    print(*dp[num])