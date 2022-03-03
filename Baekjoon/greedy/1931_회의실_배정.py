n = int(input())
li = []
res = 0

for _ in range(n):
    li.append(list(map(int, input().split())))

li = sorted(li, key=lambda x: (x[1], x[0]))

prev = 0
for i in range(n):
    if li[i][0] >= prev:
        res += 1
        prev = li[i][1]
print(res)