import sys

n = int(input())
dic = {}

for _ in range(n):
    cur = int(sys.stdin.readline())
    dic[cur] = dic.get(cur, 0) + 1

for v in sorted(dic):
    for i in range(dic[v]):
        print(v)