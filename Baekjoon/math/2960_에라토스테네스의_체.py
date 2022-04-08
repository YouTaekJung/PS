n, k = map(int, input().split())
count = 0
li = [True] * (n + 1)

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if li[j]:
            li[j] = False
            count += 1
            if count == k:
                print(j)