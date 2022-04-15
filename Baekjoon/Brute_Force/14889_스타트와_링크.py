from itertools import combinations

n = int(input())
li = list(combinations(range(n), n // 2))
mat = [list(map(int, input().split())) for _ in range(n)]
s = sum(sum(mat, []))
ans = 100000

for l in li:
    li1, li2 = l, tuple(set(range(n)) - set(l))
    sum_s, sum_l = 0, 0
    for i in li1:
        for j in li1:
            sum_s += mat[i - 1][j - 1]

    for i in li2:
        for j in li2:
            sum_l += mat[i - 1][j - 1]
    ans = min(ans, abs(sum_s - sum_l))

print(ans)