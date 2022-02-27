t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, type = input().split()
        dic[type] = dic.get(type, 0) + 1
    li = list(dic.values())
    res = 1
    for l in li:
        res *= l + 1
    print(res - 1)
