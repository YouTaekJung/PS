from collections import deque
n = int(input())
q = deque(enumerate(map(int, input().split())))
res = []

while q:
    idx, num = q.popleft()
    res.append(idx + 1)
    if num > 0:
        q.rotate(1 - num)
    elif num < 0:
        q.rotate(-num)
    print(q)

print(*res)
