n, q = map(int, input().split())
li1, li2 = list(map(int, input().split())), list(map(int, input().split()))
g = []
for i in range(n - 1):
    g.append((li2[i + 1] - li2[i]) / (li1[i + 1] - li1[i]))

for _ in range(q):
    i, j = map(int, input().split())

print(g)
