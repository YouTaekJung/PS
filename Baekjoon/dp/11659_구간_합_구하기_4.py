import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + li[i - 1]

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    print(dp[y] - dp[x - 1])
