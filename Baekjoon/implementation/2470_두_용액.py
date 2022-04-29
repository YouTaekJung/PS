n = int(input())
li = sorted(list(map(int, input().split())))
left, right = 0, n - 1
prev = [li[0] + li[n - 1], [li[0], li[n - 1]]]

while left < right:
    cur = li[left] + li[right]
    if cur == 0:
        prev[1] = [li[left], li[right]]
        break
    if abs(cur) < abs(prev[0]):
        prev = [cur, [li[left], li[right]]]
    if cur < 0:
        left += 1
    else:
        right -= 1

print(*prev[1])