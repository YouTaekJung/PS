from itertools import permutations

res_max = 1000000000
res_min = -1000000000
n = int(input())
num = list(input().split())
ope_text = ['+', '-', '*', '/']
li = list(map(int, input().split()))
ope = []

for i in range(4):
    ope += [ope_text[i]] * li[i]

per = list(set(permutations(ope)))
for i in range(len(per)):
    cur = num[0]
    for j in range(len(per[i])):
        if per[i][j] == '/':
            sign = 1
            if int(cur) < 0:
                sign = -1
                cur = str(-int(cur))
            cur = str(sign * (int(cur) // int(num[j + 1])))
        else:
            cur = str(eval(cur + per[i][j] + num[j + 1]))
    cur = int(cur)
    if i == 0:
        res_max = cur
        res_min = cur
    else:
        if cur > res_max:
            res_max = cur
        if cur < res_min:
            res_min = cur

print(res_max)
print(res_min)