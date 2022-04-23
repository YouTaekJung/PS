t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    check = 0
    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            check = 1
            break
        x += m
    if check == 0:
        print(-1)
