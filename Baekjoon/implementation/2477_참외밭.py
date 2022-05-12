n = int(input())
ans = 0
li, d, l = [], [], [0, 0, 0, 0, 0]

for i in range(6):
    x, y = map(int, input().split())
    li.append(y)
    d.append(x)
    l[x] += y
li.append(li[0])
d.append(d[0])

idx = 0
for i in range(3):
    if d[i] == d[i + 2] and d[i + 1] == d[i + 3]:
        idx = i
        break
l = sorted(list(set(l)))[::-1]
ans += l[0] * (l[0] if l[1] == 0 else l[1])
ans -= li[idx + 1] * li[idx + 2]
print(ans * n)