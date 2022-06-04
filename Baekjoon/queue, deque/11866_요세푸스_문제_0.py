# import sys
# n, k = map(int, sys.stdin.readline().split())
# li = list(range(1, n + 1))
# res = []
# i = 0
# while len(li):
#     for j in range(k - 1):
#         i += 1
#         if i == (len(li) - 1):
#             i = 0
#     res.append(li[i])
#     li.remove(li[i])
# print(res)
#
from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))
ans = []

i = 1
while q:
    cur = q.popleft()
    if i != k:
        q.append(cur)
    else:
        ans.append(str(cur))
        i = 0
    i += 1

print(f"<{', '.join(ans)}>")