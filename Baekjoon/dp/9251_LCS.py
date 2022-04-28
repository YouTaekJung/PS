li_a, li_b = input(), input()
dp = [[0] * (len(li_b) + 1) for _ in range(len(li_a) + 1)]

for i in range(len(li_a)):
    for j in range(len(li_b)):
        if li_a[i] == li_b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j], dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])