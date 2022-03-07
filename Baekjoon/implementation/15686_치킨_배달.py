from itertools import combinations

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            house.append([i, j])
        if mat[i][j] == 2:
            chicken.append([i, j])

for i in range(len(house)):
    temp = []
    for j in range(len(chicken)):
        count = 0
        count += abs(house[i][0] - chicken[j][0])
        count += abs(house[i][1] - chicken[j][1])
        temp.append(count)
    house[i] = temp

com = list(combinations(range(len(chicken)), m))
res = 100000

for c in com:
    cur = 0
    for i in range(len(house)):
        temp = []
        for j in range(len(c)):
            temp.append(house[i][c[j]])
        cur += min(temp)
    res = min(res, cur)
print(res)