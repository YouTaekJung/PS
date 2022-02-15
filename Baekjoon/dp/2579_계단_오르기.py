n = int(input())
li = [0]

for _ in range(n):
    li.append(int(input()))

if len(li) == 2:
    print(li[1])
else:
    dp = [0, li[1], li[1] + li[2]] + [0] * (n - 2)

    for i in range(3, len(li)):
        dp[i] = max(dp[i - 3] + li[i - 1] + li[i], dp[i - 2] + li[i])

    print(dp[-1])