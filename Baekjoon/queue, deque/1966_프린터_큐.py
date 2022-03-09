from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    li = input().split()
    q = deque(list(map(lambda i: [int(li[i]), i], range(len(li)))))
    count = 0

    while True:
        cur = q.popleft()

        if any(cur[0] < x[0] for x in q):
            q.append(cur)
        else:
            count += 1
            if cur[1] == m:
                print(count)
                break