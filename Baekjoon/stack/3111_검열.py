from collections import deque
a, t = input(), deque(list(input()))
front, back = [], []
check = 1

while t:
    if check:
       t.popleft()

    else:

    check *= -1
