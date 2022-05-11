from collections import deque

n = int(input())
tree = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    tree[x].append((y, w))
    tree[y].append((x, w))

def bfs(node):
    q = deque([[node, 0]])
    visited = [0] * (n + 1)
    visited[node] = 1
    res = [0, 0]
    while q:
        cur, c = q.popleft()
        for t in tree[cur]:
            next, v = t
            if visited[next] == 0:
                visited[next] = 1
                q.append((next, c + v))
                if res[1] < c + v:
                    res[0] = next
                    res[1] = c + v

    return res

s = bfs(1)
e = bfs(s[0])
print(e[1])