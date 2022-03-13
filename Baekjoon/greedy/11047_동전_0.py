n, k = map(int, input().split())
li = []
res = 0

for i in range(n):
    li.append(int(input()))

for i in range(n - 1, -1, -1):
    if k // li[i] != 0:
        res += k // li[i]
        k -= k // li[i] * li[i]
    if k == 0:
        break

print(res)