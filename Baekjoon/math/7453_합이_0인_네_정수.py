import sys
input = sys.stdin.readline

n = int(input())
mat = [[] for _ in range(4)]
for _ in range(n):
    li = list(map(int, input().split()))
    for i in range(4):
        mat[i].append(li[i])

d, ans = {}, 0
for i in mat[0]:
    for j in mat[1]:
        d[i + j] = d.get(i + j, 0) + 1

for i in mat[2]:
    for j in mat[3]:
        if -(i + j) in d:
            ans += d[-(i + j)]

print(ans)
