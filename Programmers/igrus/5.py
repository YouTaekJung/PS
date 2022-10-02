n = int(input())
li = sorted(list(map(int, input().split())))
ans = li[-1] - li[0]

for i in range(n - 1):
    ans += li[i + 1] - li[i]
print(ans)