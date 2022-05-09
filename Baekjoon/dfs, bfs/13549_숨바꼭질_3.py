from collections import deque

n, k = map(int, input().split())
q = deque([[n, 0]])
visited = [0] * 100001

while q:
    x, c = q.popleft()
    visited[x] = 1
    if x == k:
        print(c)
        break
    if 2 * x < 100001 and visited[2 * x] == 0:
        q.appendleft([2 * x, c])
    if x + 1 < 100001 and visited[x + 1] == 0:
        q.append([x + 1, c + 1])
    if x - 1 >= 0 and visited[x - 1] == 0:
        q.append([x - 1, c + 1])