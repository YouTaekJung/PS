from collections import deque

n, k = map(int, input().split())
q = deque([[n, 0, []]])
visited = [0] * 100001

while q:
    x, c, li = q.popleft()
    li.append(x)
    visited[x] = 1
    if x == k:
        print(c)
        print(*li)
        break
    if 2 * x < 100001 and visited[2 * x] == 0:
        q.append([2 * x, c + 1, li[:]])
    if x + 1 < 100001 and visited[x + 1] == 0:
        q.append([x + 1, c + 1, li[:]])
    if x - 1 >= 0 and visited[x - 1] == 0:
        q.append([x - 1, c + 1, li[:]])