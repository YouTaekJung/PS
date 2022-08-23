from itertools import combinations
from bisect import bisect_left, bisect_right

n, s = map(int, input().split())
li = list(map(int, input().split()))

def find(li, s):
    return bisect_right(li, s) - bisect_left(li, s)

def com(li):
    res = []
    for i in range(1, len(li) + 1):
        for l in combinations(li, i):
            res.append(sum(l))
    return sorted(res)

left, right = li[:n // 2], li[n // 2:]
com_left, com_right, = com(left), com(right)

ans = find(com_left, s) + find(com_right, s)
for c in com_left:
    ans += find(com_right, s - c)

print(ans)