import sys

n, m = map(int, sys.stdin.readline().split())
dic1 = {}
dic2 = {}

for i in range(n):
    cur = sys.stdin.readline().split()[0]
    dic1[str(i + 1)] = cur
    dic2[cur] = i + 1

for _ in range(m):
    cur = sys.stdin.readline().split()[0]

    if cur.isdigit():
        print(dic1[cur])
    else:
        print(dic2[cur])