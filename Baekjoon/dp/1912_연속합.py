n = int(input())
li = list(map(int, input().split()))
dp = [li[0]] + [0] * (n - 1)

for i in range(1, n):
    dp[i] = max(dp[i - 1] + li[i], li[i])

print(max(dp))