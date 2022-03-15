from collections import deque
c, p = map(int, input().split())
li = list(map(int, input().split()))
res = 0

if p == 1:
    q = deque()
    for i, l in enumerate(li):
        q.append(l)
        if len(q) == 5:
            q.popleft()
        if len(q) == 4 and q[0] == q[1] == q[2] == q[3]:
            res += 1
    print(res + c)
elif p == 2:
    q = deque()
    for i, l in enumerate(li):
        q.append(l)
        if len(q) == 3:
            q.popleft()
        if len(q) == 2 and q[0] == q[1]:
            res += 1
    print(res)
elif p == 3:
    q = deque()
    for i, l in enumerate(li):
        q.append(l)
        if len(q) == 4:
            q.popleft()
        if len(q) == 3 and (q[0] == q[1] == q[2] - 1 or q[0] - 1 == q[1]):
            res += 1
    print(res)
elif p == 4:
    q = deque()
    for i, l in enumerate(li):
        q.append(l)
        if len(q) == 4:
            q.popleft()
        if len(q) == 3 and (q[0] - 1 == q[1] == q[2] or q[0] == q[1] - 1):
            res += 1
    print(res)
elif p == 5:
    q1 = deque()
    q2 = deque()
    for i, l in enumerate(li):
        q1.append(l)
        if len(q1) == 4:
            q1.popleft()
        if len(q1) == 3:
            if q1[0] == q1[1] == q1[2] or q1[0] - 1 == q1[1] == q1[2] - 1:
                res += 1
        q2.append(l)
        if len(q2) == 3:
            q2.popleft()
        if len(q2) == 2:
            if q2[0] + 1 == q2[1] or q2[0] - 1 == q2[1]:
                res += 1
    print(res)
elif p == 6:
    q1 = deque()
    q2 = deque()
    for i, l in enumerate(li):
        q1.append(l)
        if len(q1) == 4:
            q1.popleft()
        if len(q1) == 3:
            if q1[0] == q1[1] == q1[2] or q1[0] + 1 == q1[1] == q1[2]:
                res += 1
        q2.append(l)
        if len(q2) == 3:
            q2.popleft()
        if len(q2) == 2:
            if q2[0]== q2[1] or q2[0] - 2 == q2[1]:
                res += 1
    print(res)
else:
    q1 = deque()
    q2 = deque()
    for i, l in enumerate(li):
        q1.append(l)
        if len(q1) == 4:
            q1.popleft()
        if len(q1) == 3:
            if q1[0] == q1[1] == q1[2] or q1[0] == q1[1] == q1[2] + 1:
                res += 1
        q2.append(l)
        if len(q2) == 3:
            q2.popleft()
        if len(q2) == 2:
            if q2[0] == q2[1] or q2[0] == q2[1] - 2:
                res += 1
    print(res)
