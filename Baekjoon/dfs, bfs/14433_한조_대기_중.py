import sys
input = sys.stdin.readline

def dfs(num, graph, selected, visited):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or dfs(selected[g], graph, selected, visited):
            selected[g] = num
            return True
    return False

def bimatch(k):
    res = 0
    graph = [[] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1)
    selected = [-1] * (m + 1)
    for i in range(n):
        visited = [0] * (n + 1)
        if dfs(i, graph, selected, visited):
            res += 1
    return res

n, m, k1, k2 = map(int, input().split())
print('그만 알아보자' if bimatch(k1) >= bimatch(k2) else '네 다음 힐딱이')