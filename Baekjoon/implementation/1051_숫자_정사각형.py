n, m = map(int, input().split())
min_num = min(n, m)
res = 1
li = []
for _ in range(n):
    li.append(list(input()))

for i in range(min_num):
    for j in range(n - i - 1):
        for k in range(m - i - 1):
            if len(set([li[j][k], li[j+i+1][k], li[j][k+i+1], li[j+i+1][k+i+1]])) == 1:
                cur = (i + 2) ** 2
                if cur > res:
                    res = cur

print(res)