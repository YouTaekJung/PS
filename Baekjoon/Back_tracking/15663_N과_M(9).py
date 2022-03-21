n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    c = 0
    for i in range(n):
        if not visited[i] and c != li[i]:
            visited[i] = True
            temp.append(li[i])
            c = li[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()