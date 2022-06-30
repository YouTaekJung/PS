ans = [0, 0]
for i in range(1, 6):
    cur = sum(map(int, input().split()))
    if cur > ans[1]:
        ans = [i, cur]
print(*ans)