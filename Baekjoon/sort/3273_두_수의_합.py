n = int(input())
li = sorted(list(map(int, input().split())))
t = int(input())
left, right, count = 0, n - 1, 0

while left < right:
    cur = li[left] + li[right]
    if cur == t:
        count += 1
    if cur < t:
        left += 1
        continue
    right -= 1
print(count)