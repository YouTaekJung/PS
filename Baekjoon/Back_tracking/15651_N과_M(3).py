n, m = map(int, input().split())

def recur(li):
    if len(li) == m:
        print(*li)
    else:
        for i in range(1, n+1):
            temp = li[:]
            temp.append(i)
            recur(temp)
    return

recur([])