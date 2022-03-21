n, m = map(int, input().split())
li = sorted(list(set(map(int, input().split()))))
temp = []
d = {}

def dfs():
    if len(temp) == m:
        s = ' '.join(list(map(str, temp)))
        if s not in d:
            d[s] = 1
            print(s)
        return

    for i in range(len(li)):
        temp.append(li[i])
        dfs()
        temp.pop()

dfs()