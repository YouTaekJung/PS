n = int(input())
li = list(map(int, input().split()))
dp = [0] * (n - 1) + [1]
for i in range(n - 2, -1, -1):
    if li[i] == 0:
        dp[i] = dp[i + 1] + 1
    else:
        if i + li[i] + 1 >= n:
            dp[i] = 1
        else:
            dp[i] = dp[i + li[i] + 1] + 1
print(*dp)