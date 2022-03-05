from collections import deque
t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    q = deque(eval(input()))
    d = 1
    flag = 1

    for x in p:
        if x == 'R':
            d *= -1
        else:
            if len(q):
                if d == 1:
                    q.popleft()
                else:
                    q.pop()
            else:
                flag = 0
                break
    if d == -1:
        q.reverse()
    if flag:
        print(f"[{','.join(list(map(str, q)))}]")
    else:
        print('error')
