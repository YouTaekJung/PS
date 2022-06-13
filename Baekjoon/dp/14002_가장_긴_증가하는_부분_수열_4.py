from bisect import bisect_left

n = int(input())
li = list(map(int, input().split()))
dp, idx, ans = [], [], []

for l in li:
    cur = bisect_left(dp, l)
    if len(dp) <= cur:
        dp.append(l)
    else:
        dp[cur] = l
    idx.append(cur)

m = max(idx)
for i in range(len(idx) - 1, -1, -1):
    if idx[i] == m:
        ans.append(li[i])
        m -= 1

print(len(ans))
print(*ans[::-1])