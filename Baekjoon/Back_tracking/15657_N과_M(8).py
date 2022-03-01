n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

def dfs(l):
    if len(l) == m:
        print(*l)
    else:
        for i in range(n):
            if len(l) == 0 or li[i] >= l[-1]:
                temp = l[:]
                temp.append(li[i])
                dfs(temp)
    return

dfs([])