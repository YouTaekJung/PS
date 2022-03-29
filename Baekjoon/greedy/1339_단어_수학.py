n = int(input())
li = []
d = {}

for _ in range(n):
    cur = list(input())
    li.append(cur)
    for i in range(len(cur)):
        if cur[i] not in d:
            d[cur[i]] = [len(cur) - i, 10 ** (len(cur) - i - 1)]
        else:
            d[cur[i]][0] = len(cur) - i
            d[cur[i]][1] += 10 ** (len(cur) - i - 1)

temp = sorted(map(list, d.items()), key=lambda x: (-x[1][1], -x[1][0]))
for i in range(len(temp)):
    d[temp[i][0]] = 9 - i

for i, l in enumerate(li):
    li[i] = ''.join(list(map(lambda x: str(d[x]), l)))

print(sum(list(map(int, li))))