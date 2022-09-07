import sys
input = sys.stdin.readline
from math import ceil

n, m = map(int, input().split())
li = [int(input()) for _ in range(m)]
left = 1
right = ans = max(li)

while left <= right:
    mid = (left + right) // 2
    s = sum(map(lambda x: ceil(x / mid), li))
    if s <= n:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
