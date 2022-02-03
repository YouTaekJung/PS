check = [[], []]
for _ in range(3):
    li = list(map(int, input().split()))
    for i in range(2):
        if li[i] in check[i]:
            check[i].remove(li[i])
        else:
            check[i].append(li[i])
print(*check[0], *check[1])