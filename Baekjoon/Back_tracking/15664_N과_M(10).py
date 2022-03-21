n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
visited = [False] * n
temp = [0]

def dfs():
    if len(temp) == m + 1:
        print(*temp[1:])
        return
    c = 0
    for i in range(n):
        if not visited[i] and c != li[i] and temp[-1] <= li[i]:
            visited[i] = True
            temp.append(li[i])
            c = li[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()