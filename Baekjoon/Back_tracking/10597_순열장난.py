per = input()
n = (len(per) - 9) // 2 + 9 if len(per) > 9 else len(per)
check = [0] * (n + 1)
ans = []

def bt(p):
    if sum(check) == n:
        print(*ans)
        exit()
    if len(p) >= 2:
        cur = int(p[:2])
        if cur <= n and not check[cur]:
            check[cur] = 1
            ans.append(cur)
            bt(p[2:])
            check[cur] = 0
            ans.pop()
    cur = int(p[0])
    if cur <= n and not check[cur]:
        check[cur] = 1
        ans.append(cur)
        bt(p[1:])
        check[cur] = 0
        ans.pop()

bt(per)