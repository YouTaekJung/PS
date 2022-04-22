n = int(input())
li = list(map(int, input().split()))
flag = 0

def recur(l):
    global flag
    if li == l:
        flag = 1
    if flag == 1:
        print(l)
    for i in range(1 if len(l) == 0 else l[-1], n + 1):
        temp = l[:]
        temp.append(i)
        recur(temp)
    return

if li == sorted(li, reverse=True):
    print(-1)
else:
    recur([])