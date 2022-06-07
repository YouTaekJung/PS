import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    visited = [0] * 10001
    q = deque([[n, '']])
    while q:
        cur, s = q.popleft()
        if cur == m:
            print(s)
            break
        if visited[cur] == 0:
            q.append([cur * 2 % 10000, s + 'D'])
            q.append([cur - 1 if cur > 0 else 9999, s + 'S'])
            q.append([cur % 1000 * 10 + cur // 1000, s + 'L'])
            q.append([cur % 10 * 1000 + cur // 10, s + 'R'])
            visited[cur] = 1