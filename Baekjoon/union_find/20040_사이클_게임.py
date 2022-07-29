import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b, c):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[max(a, b)] = min(a, b)
    else:
        return c
    return 0

n, m = map(int, input().split())
parents = list(range(n))
ans = 0

for i in range(1, m + 1):
    x, y = map(int, input().split())
    if union_parent(parents, x, y, i):
        print(i)
        exit()

print(0)