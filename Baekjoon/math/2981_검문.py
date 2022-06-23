from itertools import combinations
from math import gcd

n = int(input())
li = sorted([int(input()) for _ in range(n)])
ans = []

g = li[1] - li[0]
for i in range(n - 1):
    g = gcd(g, li[i + 1] - li[i])

for j in range(2, int(g ** 0.5) + 1):
    if g % j == 0:
        ans.append(j)
        ans.append(g // j)

ans.append(g)
ans = sorted(list(set(ans)))
print(*ans)