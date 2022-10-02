from collections import deque

n = int(input())
q = deque([[n, 0]])
while q:
    num, count = q.popleft()
    if num == 1:
        print(count + 1)
        break
    q.append([num - 1, count + 1])
    if '1' in str(num):
        li = list(str(num))
        li.remove('1')
        num = int(''.join(li))
        if num == 0:
            print(count + 1)
            break
        q.appendleft([num, count + 1])
