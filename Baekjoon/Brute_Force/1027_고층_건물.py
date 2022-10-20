def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

n = int(input())
li = list(map(int, input().split()))
ans = 0

for i, l in enumerate(li):
    m = 0
    left = float('inf')
    right = -float('inf')
    for j in range(i - 1, -1, -1):
        s = slope(i + 1, l, j + 1, li[j])
        if s < left:
            left = s
            m += 1
    for j in range(i + 1, n):
        s = slope(i + 1, l, j + 1, li[j])
        if s > right:
            right = s
            m += 1
    ans = max(ans, m)
print(ans)