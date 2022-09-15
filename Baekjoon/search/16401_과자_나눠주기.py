m, n = map(int, input().split())
li = sorted(list(map(int, input().split())))
left, right = 0, li[-1]

ans = 0
while left <= right:
    s = 0
    mid = (left + right) // 2

    if mid == 0:
        s = 0
        break

    for l in li:
        if l >= mid:
            s += (l // mid)

    if s >= m:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)