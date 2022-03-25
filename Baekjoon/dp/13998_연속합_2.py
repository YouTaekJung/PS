n = int(input())
li = list(map(int, input().split()))
dp = [[x for x in li] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + li[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + li[i])

print(max(max(dp[0]), max(dp[1])))