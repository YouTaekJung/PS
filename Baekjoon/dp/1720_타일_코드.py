n = int(input())
dp1 = [0, 1, 3] + [0] * (n - 2)
dp2 = [0, 1, 3, 1, 5] + [0] * (n - 4)

for i in range(3, n + 1):
    dp1[i] = dp1[i - 1] + 2 * dp1[i - 2]

for i in range(5, n + 1):
    dp2[i] = dp2[i - 2] + 2 * dp2[i - 4]

print((dp1[n] + dp2[n]) // 2)