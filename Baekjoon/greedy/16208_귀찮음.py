n = int(input())
a = sorted(list(map(int, input().split())))
s = sum(a)
res = 0

for i in range(n - 1):
    s -= a[i]
    res += a[i] * s

print(res)
