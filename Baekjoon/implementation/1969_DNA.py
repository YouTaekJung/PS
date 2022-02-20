n, m = map(int, input().split())
li = []
res = [{} for _ in range(m)]

for _ in range(n):
    li.append(input())

for i in range(n):
    for j in range(m):
        if li[i][j] in res[j]:
            res[j][li[i][j]] += 1
        else:
            res[j][li[i][j]] = 1

hd = ''.join(list(map(lambda x: sorted(list(x.items()),key=lambda y: (-y[1], y[0]))[0][0], res)))
print(hd)

count = 0
for l in li:
    for j in range(m):
        if hd[j] != l[j]:
            count += 1
print(count)
