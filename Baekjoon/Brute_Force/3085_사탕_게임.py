n = int(input())
li = []
res = 0

def c():
    res1, res2 = 1, 1
    for i in range(n):
        count1, count2 = 1, 1
        for j in range(n - 1):
            if li[i][j] == li[i][j + 1]:
                count1 += 1
                res1 = max(count1, res1)
            else:
                count1 = 1
            if li[j][i] == li[j + 1][i]:
                count2 += 1
                res2 = max(count2, res2)
            else:
                count2 = 1
    return max(res1, res2)

for _ in range(n):
    li.append(list(input()))

for i in range(n):
    for j in range(n - 1):
        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        res = max(res, c())
        li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        li[j][i], li[j+1][i] = li[j+1][i], li[j][i]
        res = max(res, c())
        li[j][i], li[j+1][i] = li[j+1][i], li[j][i]
print(res)