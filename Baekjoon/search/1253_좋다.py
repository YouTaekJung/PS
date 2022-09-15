n = int(input())
li = sorted(list(map(int, input().split())))
check = [0] * n

for cur in range(n):
    left, right = 0, n - 1
    while left < right:
        if li[left] + li[right] == li[cur]:
            check[cur] = 1
            left += 1
        elif li[left] + li[right] > li[cur]:
            right -= 1
        else:
            left += 1
print(check.count(1))