n, m = map(int, input().split())
dic1 = {}
dic2 = {}

for i in range(n):
    cur = input()
    dic1[str(i + 1)] = cur
    dic2[cur] = i + 1

for _ in range(m):
    cur = input()
    if cur.isdigit():
        print(dic1[cur])
    else:
        print(dic2[cur])