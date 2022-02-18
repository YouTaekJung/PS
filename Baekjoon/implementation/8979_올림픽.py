n, k = map(int, input().split())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

li = sorted(li, key=lambda x: (-x[1], -x[2], -x[3]))

if li[0][0] == k:
    print(1)
else:
    rank = 1
    count = 1
    prev = li[0][1:]
    for i in range(1, n):
        if prev == li[i][1:]:
            count += 1
        else:
            rank += count
            count = 1
            prev = li[i][1:]
        if li[i][0] == k:
            print(rank)
            break