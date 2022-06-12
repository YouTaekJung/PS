n = int(input())
li = []
w = h = w2 = h2 = 0

for i in range(6):
    d, l = map(int, input().split())
    li.append(l)
    if i % 2 == 0:
        w = max(w, l)
    else:
        h = max(h, l)

for i in range(6):
    if not i % 2 and h == li[(i + 5) % 6] + li[(i + 1) % 6]:
        w2 = li[i]
    elif i % 2 and w == li[(i + 5) % 6] + li[(i + 1) % 6]:
        h2 = li[i]

print(n * (w * h - w2 * h2))