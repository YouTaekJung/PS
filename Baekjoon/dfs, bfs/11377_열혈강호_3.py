import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = sorted([list(map(int, input().split()))[1:] for _ in range(n)], key=lambda x: -len(x))
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

for i in range(n):
    visited = [0] * n
    bimatch(i)

for i in range(n):
    visited = [0] * n
    if bimatch(i):
        k -= 1
    if not k:
        break
print(m - selected.count(-1) + 1)