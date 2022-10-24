from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
while True:
    m = int(input())
    if m == -1:
        print(*q if len(q) else "empty")
        break
    elif m == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(m)
