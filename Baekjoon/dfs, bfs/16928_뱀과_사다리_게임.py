from collections import deque

n, m = map(int, input().split())
d = {}
visited = [0] * 101
visited[1] = 1
q = deque([[1, 0]])
ans = 100

for _ in range(n + m):
    x, y = map(int, input().split())
    d[x] = y

while q:
    cur, count = q.popleft()
    if cur == 100:
        ans = min(ans, count)
        continue

    for i in range(cur + 1, min(101, cur + 7)):
        if visited[i] == 0:
            visited[i] = 1
            if i in d:
                q.append([d[i], count + 1])
            else:
                q.append([i, count + 1])

print(ans)