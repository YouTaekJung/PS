t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()

    sorted_li = [0] * n
    for i in range(n):
        if i % 2:
            sorted_li[i // 2] = li[i]
        else:
            sorted_li[n - (i // 2) - 1] = li[i]

    res = 0
    for i in range(n - 1):
        res = max(res, abs(sorted_li[i] - sorted_li[i + 1]))

    print(res)