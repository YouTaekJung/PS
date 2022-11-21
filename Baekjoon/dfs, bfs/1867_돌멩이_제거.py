def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            return True
    return False

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)

selected = [-1] * (n)
ans = 0
for i in range(n):
    visited = [0] * n
    if bimatch(i):
        ans += 1
print(ans)

