n, p = map(int, input().split())
ans = []
cur = n

while True:
    cur = (cur * n) % p
    if cur in ans:
        print(len(ans) - ans.index(cur))
        break
    ans.append(cur)