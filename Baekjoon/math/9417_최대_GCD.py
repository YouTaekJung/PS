from itertools import combinations

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input())
for _ in range(n):
    li = list(map(int, input().split()))
    com = list(combinations(li, 2))
    m = 1
    for c in com:
        m = max(m, gcd(c[0], c[1]))
    print(m)