n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
m = [1, 0]

for _ in range(n):
    cur = list(map(int, input().split()))
    num, li = cur[0], cur[1:-1]
    for i in range(0, len(li), 2):
        tree[num].append([li[i], li[i + 1]])

def dfs(s, d):
    global m
    if d > m[1]:
        m = [s, d]
    visited[s] = 1
    for t in tree[s]:
        if visited[t[0]] == 0:
            dfs(t[0], t[1] + d)

dfs(1, 0)
visited = [0] * (n + 1)
dfs(m[0], 0)
print(m[1])
