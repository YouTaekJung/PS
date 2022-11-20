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

n, m = map(int, input().split())
li1 = [int(input()) for _ in range(n)]
li2 = [int(input()) for _ in range(m)]
graph = [[] for _ in range(n)]

for i, l1 in enumerate(li1):
    for j, l2 in enumerate(li2):
        if l1 / 2 <= l2 <= l1 * 3 / 4 or l1 <= l2 <= l1 * 5 / 4:
            graph[i].append(j)

ans = 0
selected = [-1] * (m + 1)
for i in range(n):
    visited = [0] * n
    if bimatch(i):
        ans += 1

print(ans)