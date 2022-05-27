n = int(input())
li = list(map(int, input().split()))
left, right = 0, n - 1
ans = [2 * 10 ** 9 + 1, 0, 0]

while left < right:
    l, r = li[left], li[right]
    if abs(l + r) < ans[0]:
        ans = [abs(l + r), l , r]
    if l + r == 0:
        break
    elif l + r < 0:
        left += 1
    else:
        right -= 1

print(*ans[1:])