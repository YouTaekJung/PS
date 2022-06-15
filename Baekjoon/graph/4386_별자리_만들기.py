import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
parent = list(range(n + 1))

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

v = []
total_cost = 0

for i in range(1, n + 1):
    a, b = map(float, input().split())
    v.append((i, a, b))

com = list(combinations(v, 2))
edges = []
for c in com:
    cost = ((c[0][1] - c[1][1]) ** 2 + (c[0][2] - c[1][2]) ** 2) ** 0.5
    edges.append([cost, c[0][0], c[1][0]])
edges.sort()

for i in range(len(com)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(round(total_cost, 2))