n = int(input())

li = [0] * n
for i in range(n):
    li[i] = list(map(int, input().split()))
res = [1] * n

for i in range(n):
    for j in range(n):
        if li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            res[j] += 1

print(' '.join(map(str, res)))