from collections import deque

n, m = map(int, input().split())
li = list(map(int, input().split()))
q = deque(range(1, n + 1))
count = 0

for l in li:
    if len(q) // 2 < q.index(l):
        while True:
            p = q.pop()
            if p == l:
                count += 1
                break
            q.insert(0, p)
            count += 1
    else:
        while True:
            p = q.popleft()
            if p == l:
                break
            q.append(p)
            count += 1
print(count)