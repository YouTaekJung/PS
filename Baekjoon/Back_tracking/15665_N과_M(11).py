n, m = map(int, input().split())
li = sorted(list(set(map(int, input().split()))))
temp = []
cache = []

def dfs():
    if len(temp) == m:
        cache.append(' '.join(list(map(str, temp))))
        return

    for i in range(len(li)):
        temp.append(li[i])
        c = li[i]
        dfs()
        temp.pop()

dfs()

cache = sorted(list(set(cache)))
for c in cache:
    print(c)