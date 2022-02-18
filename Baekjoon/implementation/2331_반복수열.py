a, p = map(int, input().split())
li = [str(a)]

cur = str(a)
while True:
    cur = str(sum(list(map(lambda x: int(x) ** p, list(cur)))))
    if cur in li:
        print(li.index(cur))
        break
    li.append(cur)
