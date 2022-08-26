import sys
input = sys.stdin.readline

n, c = map(int, input().split())
li = sorted([int(input()) for _ in range(n)])
left, right = 1, li[-1] - li[0]
ans = 0

if c == 2:
    print(li[-1] - li[0])
else:
    while left < right:
        mid = (left + right) // 2
        count = 1
        temp = li[0]
        for i in range(n):
            if li[i] - temp >= mid:
                count += 1
                temp = li[i]
        if count >= c:
            ans = mid
            left = mid + 1
        else:
            right = mid
    print(ans)