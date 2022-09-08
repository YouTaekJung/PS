import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
left = 1
right = ans = max(li) * m

while left <= right:
    mid = (left + right) // 2
    if sum(map(lambda x: mid // x, li)) >= m:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)
