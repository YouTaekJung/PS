n, m = map(int, input().split())
d = {}
for _ in range(n):
    x, y = input().split()
    d[x] = y

for _ in range(m):
    print(d[input()])