n, r, c = map(int, input().split())
res = 0

while n > 0:
    if r >= 2 ** (n - 1):
        res += 2 ** n * 2 ** (n - 1)
    if c >= 2 ** (n - 1):
        res += 2 ** (n - 1) * 2 ** (n - 1)
    r %= 2 ** (n - 1)
    c %= 2 ** (n - 1)
    n -= 1
print(res)