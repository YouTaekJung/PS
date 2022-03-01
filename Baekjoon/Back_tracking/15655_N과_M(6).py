n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

def dfs(l):
    if len(l) == m:
        print(*l)
    if len(l) == 0:
        for i in range(n):
            if li[i] not in l:
                temp = l[:]
                temp.append(li[i])
                dfs(temp)
    else:
        for i in range(n):
            if li[i] not in l and li[i] >= l[-1]:
                temp = l[:]
                temp.append(li[i])
                dfs(temp)
    return

dfs([])