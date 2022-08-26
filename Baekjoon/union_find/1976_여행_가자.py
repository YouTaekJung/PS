import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
p = list(range(n + 1))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j]:
            union_parent(p, i + 1, j + 1)

road = list(map(int, input().split()))
for i in range(m - 1):
    if find_parent(p, road[i]) != find_parent(p, road[i + 1]):
        print('NO')
        exit()
print('YES')