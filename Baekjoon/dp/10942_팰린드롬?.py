import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for l in range(n):
    for s in range(n - l):
        e = s + l
        
        if s == e:
            dp[s][e] = 1
        elif li[s] == li[e]:
            if s + 1 == e or dp[s + 1][e - 1] == 1:
                dp[s][e] = 1
            
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])