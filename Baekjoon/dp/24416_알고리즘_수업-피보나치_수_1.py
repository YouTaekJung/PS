n = int(input())
ans = [0, 1]
dp_li = [0, 1, 1]

def recur(n):
    global ans
    if n < 3:
        ans[0] += 1
        return 1
    else: return recur(n - 1) + recur(n - 2)

def dp(n):
    global ans, dp_li
    if n < 3: return dp_li[n]
    for i in range(3, n):
        ans[1] += 1
        dp_li.append(dp_li[i - 1] + dp_li[i - 2])
    return dp_li[-1]

recur(n)
dp(n)
print(*ans)