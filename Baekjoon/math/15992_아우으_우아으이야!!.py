import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = 0

for _ in range(n - 1):
    x, y = map(int, input().split())
    if x > li[1]:
        ans += li[1] - li[0]
        li = [x, y]
    else:
        li = [min(li[0], x), max(li[1], y)]

print(ans + li[1] - li[0])