n, m = map(int, input().split())
li = list(map(int, input().split()))
left, right = 0, 0
acc = li[left]
ans = n
flag = 0

while left <= right and right < n:
    if acc >= m:
        flag = 1
        ans = min(ans, right - left + 1)
        acc -= li[left]
        left += 1
    else:
        right += 1
        if right < n:
            acc += li[right]

print(ans if flag else 0)