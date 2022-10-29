import sys
input = sys.stdin.readline

g, p = int(input()), int(input())
li = [int(input()) for _ in range(p)]
parent = [i for i in range(g + 1)]
ans = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for l in li:
    cur = find(l)
    if cur == 0:
        break
    parent[cur] = parent[cur - 1]
    ans += 1
print(ans)