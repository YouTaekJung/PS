from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))
res = []

count = 1
while len(q):
    p = q.popleft()
    if count < k:
        q.append(p)
        count += 1
    else:
        res.append(str(p))
        count = 1
print(f"<{', '.join(res)}>")