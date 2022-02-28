from collections import deque


def bfs(v):
    q = deque([[v, 0]])
    while q:
        num, count = q.popleft()
        if not visited[num]:
            visited[num] = True
            if num == k:
                return count
            count += 1
            if (num * 2) <= 100000:
                q.append([num * 2, count])
            if (num + 1) <= 100000:
                q.append([num + 1, count])
            if (num - 1) >= 0:
                q.append([num - 1, count])
    return count


n, k = map(int, input().split())
visited = [False] * 100001
print(bfs(n))