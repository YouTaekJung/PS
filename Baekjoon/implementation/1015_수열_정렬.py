n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
check = [1] * n
res = []

for num in a:
    for i, s in enumerate(sorted_a):
        if s == num and check[i] == 1:
            res.append(i)
            check[i] = 0
            break

print(*res)