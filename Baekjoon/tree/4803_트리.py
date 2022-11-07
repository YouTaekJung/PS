import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[max(a, b)] = min(a, b)
    edge_count[min(a, b)] = edge_count.get(min(a, b), 0) + 1

i = 1
while True:
    n, m = map(int, input().split())
    if not n + m:
        break
    parent = list(range(n))
    node_count, edge_count = {}, {}
    for _ in range(m):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        union_parent(x - 1, y - 1)
    for j, p in enumerate(parent):
        parent_p = find_parent(p)
        if p != parent_p and p in edge_count:
            edge_count[parent_p] += edge_count[p]
            del edge_count[p]
        parent[j] = p = parent_p
        node_count[p] = node_count.get(p, 0) + 1

    ans = 0
    for node in set(parent):
        if node not in edge_count or node_count[node] > edge_count[node]:
            ans += 1
    if ans == 0:
        print(f'Case {i}: No trees.')
    elif ans == 1:
        print(f'Case {i}: There is one tree.')
    else:
        print(f'Case {i}: A forest of {ans} trees.')
    i += 1
