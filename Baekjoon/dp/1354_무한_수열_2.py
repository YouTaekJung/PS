n, p, q, x, y = map(int, input().split())
dp = {}

def recur(num):
    if num <= 0:
        dp[num] = 1
        return dp[num]
    if num in dp:
        return dp[num]

    dp[num] = recur(num // p - x) + recur(num // q - y)
    return dp[num]

print(recur(n))