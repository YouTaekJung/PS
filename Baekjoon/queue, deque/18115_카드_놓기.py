from collections import deque

n = int(input())
q = deque(map(int, input().split()))
after = deque(range(1, n + 1))
before = deque()

while q:
    p = q.pop()
    a = after.popleft()
    if p == 1:
        before.appendleft(a)
    elif p == 2:
        before.insert(1, a)
    elif p == 3:
        before.append(a)
print(*before)