n, k = int(input()), int(input())
left, right = 1, k

while left <= right:
    mid = (left + right) // 2
    if sum([min(mid // i, n) for i in range(1, n + 1)]) >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)