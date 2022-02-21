t = int(input())

for _ in range(t):
    center = list(map(int, input().split()))
    n = int(input())
    res = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = ((center[0] - cx) ** 2 + (center[1] - cy) ** 2) ** 0.5 - r
        d2 = ((center[2] - cx) ** 2 + (center[3] - cy) ** 2) ** 0.5 - r
        if d1 * d2 < 0:
            res += 1
    print(res)