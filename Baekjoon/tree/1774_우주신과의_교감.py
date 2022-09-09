import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
cor = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
graph = []
parent = list(range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        cost = ((cor[i][1] - cor[j][1]) ** 2 + (cor[i][0] - cor[j][0]) ** 2) ** 0.5
        graph.append((cost, i, j))
graph.sort()

ans = 0
for g in graph:
	if find_parent(parent, g[1]) != find_parent(parent, g[2]):
		union_parent(parent, g[1], g[2])
		ans += g[0]
print('%.2f' %(ans))