n, p, q = map(int, input().split())
dp = {0: 1}

def recur(num):
    if num in dp:
        return dp[num]

    dp[num] = recur(num // p) + recur(num // q)
    return dp[num]

print(recur(n))