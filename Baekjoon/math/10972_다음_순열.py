n = int(input())
li = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if li[i] > li[i - 1]:
        li[i - 1] = min([v for v in li[i:] if v > li[i - 1]])
        temp = set(range(1, n + 1)) - set(li[:i])
        li = li[:i] + sorted(list(temp))
        print(*li)
        break
else:
    print(-1)
