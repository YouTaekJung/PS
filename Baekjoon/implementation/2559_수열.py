n, k = map(int, input().split())
li = list(map(int, input().split()))
dp = [sum(li[:k])]

for i in range(k, n):
    dp.append(dp[i - k] - li[i - k] + li[i])
print(max(dp))