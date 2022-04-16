n, m = map(int, input().split())
li = list(map(int, input().split()))
visited = [False] * n
temp = []
temp_count = 0
count = 0

def dfs(s):
    global temp_count, count
    if len(temp) > 0 and temp_count == m:
        count += 1
    for i in range(s, n):
        if not visited[i]:
            visited[i] = True
            temp.append(li[i])
            temp_count += li[i]
            dfs(i + 1)
            visited[i] = False
            temp_count -= li[i]
            temp.pop()

dfs(0)
print(count)