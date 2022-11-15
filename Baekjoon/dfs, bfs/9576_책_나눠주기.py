import sys
input = sys.stdin.readline

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    selected = [-1] * (n + 1)

    for i in range(m):
        x, y = map(int, input().split())
        graph[i] = list(range(x, y + 1))

    ans = 0
    for i in range(m):
        visited = [0] * (m + 1)
        if bimatch(i):
            ans += 1
    print(ans)
