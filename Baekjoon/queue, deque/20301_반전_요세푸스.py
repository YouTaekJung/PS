from collections import deque

n, k, m = map(int, input().split())
q = deque(range(1, n + 1))
ans = []

i = d = 1
count = 0
while q:
    if d == 1:
        cur = q.popleft()
        if i != k:
            q.append(cur)
        else:
            ans.append(str(cur))
            i = 0
            count += 1
    else:
        cur = q.pop()
        if i != k:
            q.appendleft(cur)
        else:
            ans.append(str(cur))
            i = 0
            count += 1
    if count == m:
        d *= -1
        count = 0
    i += 1

for a in ans:
    print(a)