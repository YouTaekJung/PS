n, m = map(int, input().split())
li = list(map(int, input().split()))
start, end = 1, max(li)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for l in li:
        if l >= mid:
            count += l - mid

    if count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)