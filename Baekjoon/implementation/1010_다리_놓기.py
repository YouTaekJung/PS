n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    res = 1
    i = 0
    while i < n:
        res *= (m - i)
        i += 1
    while n > 1:
        res //= n
        n -= 1
    print(res)