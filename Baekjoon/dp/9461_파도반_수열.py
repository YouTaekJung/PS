t = int(input())
dp = [1, 1, 1, 2, 2]

li = []
m = 0

for _ in range(t):
    n = int(input())
    li.append(n)
    m = max(m, n)

i = 4
while len(dp) < m:
    dp.append(dp[i] + dp[i - 4])
    i += 1

for l in li:
    print(dp[l - 1])