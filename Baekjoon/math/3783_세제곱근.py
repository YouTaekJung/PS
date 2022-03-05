from decimal import *
getcontext().prec = 1000
t = int(input())

for _ in range(t):
    n = input().rstrip() + '.0000000000'
    res = round(Decimal(Decimal(n) ** (Decimal(1) / Decimal(3))), 500)
    res = Decimal(res).quantize(Decimal('.0000000001'), rounding=ROUND_DOWN)
    print(res)