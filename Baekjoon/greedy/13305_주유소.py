n = int(input())
d = list(map(int, input().split()))[::-1]
p = list(map(int, input().split()))[:-1][::-1]
res = [0] * (n - 1)
res[0] = d[0] * p[0]

for i in range(1, n - 1):
    res[i] = min(sum(d[:i + 1]) * p[i], res[i - 1] + d[i] * p[i])

print(res[-1])