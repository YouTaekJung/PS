from bisect import bisect_left

n = int(input())
li = list(map(int, input().split()))
dp = []

for l in li:
    cur = bisect_left(dp, l)
    if len(dp) <= cur:
        dp.append(l)
    else:
        dp[cur] = l

print(len(dp))