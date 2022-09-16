from collections import deque

n = int(input())
li = list(map(lambda x: 1 if x == 'O' else 0, input().split()))

def win(li):
    return True if sum([li[2 * i] - li[2 * i + 1] for i in range(n)]) > 0 else False

q = deque([[li, 0]])
while q:
    cur, count = q.popleft()
    if win(cur):
        print(count)
        break
    for i in range(count + 1, 2 * n):
        temp = [cur[i]] + cur[:i] + cur[i + 1:]
        q.append([temp, count + 1])

