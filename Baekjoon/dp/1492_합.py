from math import factorial as fac
n, k = map(int, input().split())
dp = [n] + [0] * k

for i in range(1, k + 1):
    cur = (n + 1) ** (i + 1) - 1
    for j in range(i + 1, 1, -1):
        cur -= dp[i + 1 - j] * fac(i + 1) // fac(i + 1 - j) // fac(j)
    dp[i] = cur // (i + 1)
print(dp[-1] % 1000000007)