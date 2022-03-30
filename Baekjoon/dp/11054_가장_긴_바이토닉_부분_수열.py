n = int(input())
li = list(map(int, input().split()))
re_li = li[:][::-1]
inc_dp = [1] * n
dec_dp = [1] * n

for i in range(1, n):
    inc_dp[i] = max([0] + [inc_dp[j] for j in range(i) if li[j] < li[i]]) + 1
    dec_dp[i] = max([0] + [dec_dp[j] for j in range(i) if re_li[j] < re_li[i]]) + 1

print(max([inc_dp[i] + dec_dp[::-1][i] for i in range(n)]) - 1)