n = int(input())
li = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    dp[i] = max([0] + [dp[j] for j in range(i) if li[j] < li[i]]) + 1

print(max(dp))