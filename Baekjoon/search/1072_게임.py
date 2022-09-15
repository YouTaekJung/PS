x, y = map(int, input().split())
rate = (y * 100) // x
left, right = 1, x

ans = -1
while left <= right:
    mid = (left + right) // 2
    if (mid + y) * 100 // (mid + x) <= rate:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
print(ans)