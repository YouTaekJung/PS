n, k = map(int, input().split())
li = []
for i in range(1, n + 1):
    if not n % i:
        li.append(i)
print(0 if k > len(li) else li[k-1])