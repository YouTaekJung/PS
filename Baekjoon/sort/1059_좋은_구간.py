l = int(input())
li = sorted(list(map(int, input().split())) + [0])
t = int(input())

ans = 0
for i in range(len(li) - 1):
    if li[i] == t or li[i + 1] == t:
        ans = 0
        break
    elif li[i] < t < li[i + 1]:
        ans = (t - li[i]) * (li[i + 1] - t) - 1
        break

print(ans)