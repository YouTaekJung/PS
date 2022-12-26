import sys
sys.setrecursionlimit(10 ** 6)

def dfs(s):
    global ans
    visited[s] = 1
    temp.append(s)
    cur = li[s]
    if visited[cur]:
        if cur in temp:
            ans += temp[temp.index(cur):]
        return
    else:
        dfs(cur)

for _ in range(int(input())):
    n = int(input())
    li = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    ans = []

    for i in range(1, n + 1):
        if not visited[i]:
            temp = []
            dfs(i)

    print(n - len(ans))