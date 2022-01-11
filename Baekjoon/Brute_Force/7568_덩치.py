n = int(input())

li = [0]*n
sorted_li = [[i, 0] for i in range(n)]

for i in range(n):
    li[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        if li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            sorted_li[j][1] += 1
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            sorted_li[i][1] += 1

sorted_li = sorted(sorted_li, key=lambda x: x[1])
res = sorted_li[0][0] + [0] * (n - 1)
cur = [sorted_li[0][1], 1]

for i in range(1, n):
    res[i]
