import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
s = list(range(n + 1))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_num(parent, x, y):
    if x == y or find_parent(parent, x) == find_parent(parent, y):
        print("YES")
    else:
        print("NO")

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union_parent(s, a, b)
    else:
        find_num(s, a, b)