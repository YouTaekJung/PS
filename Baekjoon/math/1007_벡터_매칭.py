from itertools import combinations
import sys
input = sys.stdin.readline

def colsum(mat):
    res = [0, 0]
    for m in mat:
        res[0] += m[0]
        res[1] += m[1]
    return res



t = int(input())
for _ in range(t):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    ans, s = 1e9, colsum(li)
    com = combinations(li, n // 2)
    for c in com:
        cur = colsum(list(c))
        ans = min(ans, ((2 * cur[0] - s[0]) ** 2 + (2 * cur[1] - s[1]) ** 2) ** 0.5)
    print(ans)
