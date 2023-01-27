n = int(input())
li = sorted(list(map(int, input().split())))

prev = li[0]
group, temp = [], [li[0]]
for i in range(1, n):
    cur = li[i]
    if prev + 1 == cur:
        temp.append(cur)
        prev = cur
    else:
        group.append(temp[0])
        temp = [cur]
        prev = cur
print(sum(group) + temp[0])
