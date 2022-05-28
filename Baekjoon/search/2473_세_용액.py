n = int(input())
li = list(map(int, input().split()))
fix, left, right = 0, 1, n - 1
ans = [3 * 10 ** 9 + 1, 0, 0, 0]

li.sort()
while fix < n:
    while left < right:
        f, l, r = li[fix], li[left], li[right]
        if abs(f + l + r) < ans[0]:
            ans = [abs(f + l + r), f, l, r]
        if f + l + r == 0:
            print(*ans[1:])
            exit()
        elif f + l + r < 0:
            left += 1
        else:
            right -= 1
    fix += 1
    left = fix + 1
    right = n - 1

print(*ans[1:])