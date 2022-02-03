m, n = map(int, input().split())

li = [0, 0] + [1] * (n - 1)

for i in range(2, n+1):
    if li[i]:
        for j in range(2*i, n+1, i):
            li[j] = 0

for i in range(m, n+1):
    if li[i]:
        print(i)