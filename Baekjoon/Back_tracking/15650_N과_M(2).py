n, m = map(int, input().split())

res = []
done = []
def recur():
    if len(res) == m:
        if sorted(res) not in done:
            print(*res)
            done.append(sorted(res))
        return
    for i in range(1, n + 1):
        if i not in res:
            res.append(i)
            recur()
            res.pop()

recur()