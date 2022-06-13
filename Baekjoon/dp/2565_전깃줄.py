from bisect import bisect_left

n = int(input())
li = sorted([list(map(int, input().split())) for _ in range(n)])
li = list(map(lambda x: x[1], li))
dp = []

for l in li:
    cur = bisect_left(dp, l)
    if len(dp) <= cur:
        dp.append(l)
    else:
        dp[cur] = l

print(len(li) - len(dp))