n = int(input())
li = sorted(list(map(int, input().split())))

prev = li[0]
ans, temp = 0, [li[0]]
for i in range(1, n):
    cur = li[i]
    if prev + 1 == cur:
        temp.append(cur)
        prev = cur
    else:
        ans += temp[0]
        temp = [cur]
        prev = cur
print(ans + temp[0])
