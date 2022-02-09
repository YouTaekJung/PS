n, x = map(int, input().split())

li = list(map(int, input().split()))
for i in range(n):
    if li[i] < x:
        print(li[i], end = " ")