n, m = map(int, input().split())
li = sorted(list(set(map(int, input().split()))))
temp = [0]
d = {}

def dfs():
    if len(temp) == m + 1:
        s = ' '.join(list(map(str, temp[1:])))
        if s not in d:
            d[s] = 1
            print(s)
        return

    for i in range(len(li)):
        if temp[-1] <= li[i]:
            temp.append(li[i])
            dfs()
            temp.pop()

dfs()