import math
m, n = map(int, input().split())
check = [1 for i in range(n - m + 1)]

for i in range(2, math.floor(n ** 0.5) + 1):
    num = m // i**2
    while num * (i**2) <= n:
        if 0 <= num * (i**2) - m <= n - m:
            check[num * (i**2) - m] = 0
        num += 1

print(sum(check))
