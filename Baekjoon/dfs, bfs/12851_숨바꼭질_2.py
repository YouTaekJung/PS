from collections import deque

n, k = map(int, input().split())
q = deque([[n, 0]])
visited = [0] * 100001
ans = [100000, 0]

while q:
    x, c = q.popleft()
    visited[x] = 1
    if x == k:
        if ans[0] > c:
            ans = [c, 1]
        elif ans[0] == c:
            ans[1] += 1
        continue
    if 2 * x < 100001 and visited[2 * x] == 0:
        q.append([2 * x, c + 1])
    if x + 1 < 100001 and visited[x + 1] == 0:
        q.append([x + 1, c + 1])
    if x - 1 >= 0 and visited[x - 1] == 0:
        q.append([x - 1, c + 1])

print(ans[0])
print(ans[1])