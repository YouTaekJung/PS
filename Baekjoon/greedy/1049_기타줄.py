n, m = map(int, input().split())
li1, li2, ans = [], [], 0
for _ in range(m):
    a, b = map(int, input().split())
    li1.append(a)
    li2.append(b)
li1.sort()
li2.sort()

if li1[0] <= li2[0] * 6:
    ans = li1[0] * (n // 6) + li2[0] * (n % 6)
    if li1[0] < li2[0] * (n % 6):
        ans = li1[0] * (n // 6 + 1)
else:
    ans = li2[0] * n

print(ans)