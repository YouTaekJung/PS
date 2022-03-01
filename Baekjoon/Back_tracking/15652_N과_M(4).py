n, m = map(int, input().split())

def recur(li):
    if len(li) == m:
        print(*li)
    else:
        for i in range(1 if len(li) == 0 else li[-1], n+1):
            temp = li[:]
            temp.append(i)
            recur(temp)
    return

recur([])

# n, m = map(int, input().split())
#
# s = []
#
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(start, n + 1):
#         s.append(i)
#         dfs(i)
#         s.pop()
#
#
# dfs(1)