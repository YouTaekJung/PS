n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for l in li:
    for i in range(1, k + 1):
        if i >= l:
            dp[i] += dp[i - l]
print(dp[-1])