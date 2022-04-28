t = int(input())

for _ in range(t):
    n = int(input())
    li = [list(map(int, input(). split())) for _ in range(2)]
    dp = [[li[0][0], li[1][0]], [li[1][0] + li[0][1], li[0][0] + li[1][1]]]
    for i in range(2, n):
        a = max(max(dp[i - 2][0], dp[i - 2][1]) + li[0][i], dp[i - 1][1] + li[0][i])
        b = max(max(dp[i - 2][0], dp[i - 2][1]) + li[1][i], dp[i - 1][0] + li[1][i])
        dp.append([a, b])

    print(max(dp[-1]))