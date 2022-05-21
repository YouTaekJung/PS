import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split()))
dp1, dp2 = first[:], first[:]

for _ in range(n - 1):
    cur = list(map(int, input().split()))
    temp00 = cur[0] + max(dp1[0], dp1[1])
    temp10 = cur[0] + min(dp2[0], dp2[1])
    temp01 = cur[1] + max(dp1[0], dp1[1], dp1[2])
    temp11 = cur[1] + min(dp2[0], dp2[1], dp2[2])
    temp02 = cur[2] + max(dp1[1], dp1[2])
    temp12 = cur[2] + min(dp2[1], dp2[2])
    dp1 = [temp00, temp01, temp02]
    dp2 = [temp10, temp11, temp12]
print(max(dp1), min(dp2))