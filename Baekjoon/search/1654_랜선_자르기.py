n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
left, right = 1, max(li)

while right >= left:
    mid = (left + right) // 2
    temp = sum(list(map(lambda x: x // mid, li)))
    if temp >= k:
        left = mid + 1
    else:
        right = mid - 1
print(right)