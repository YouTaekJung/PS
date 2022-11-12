import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split()))[1:] for _ in range(n)]
selected = [-1] * (m + 1)

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            return True
    return False

ans = 0
for i in range(n):
    visited = [0] * n
    if bimatch(i):
        ans += 1

print(ans)