n = int(input())
li = [0] + [int(input()) for _ in range(n)]
dp = [0, li[1], li[1] + li[2]]

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + li[i - 1] + li[i], dp[i - 2] + li[i]))
print(dp[-1])