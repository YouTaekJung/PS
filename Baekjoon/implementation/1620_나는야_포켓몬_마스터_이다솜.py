n, m = map(int, input().split())
li = []

for _ in range(n):
    li.append(input())

for _ in range(m):
    cur = input()
    if cur.isdigit():
        print(li[int(cur) - 1])
    else:
        print(li.index(cur) + 1)