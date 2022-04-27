n = int(input())
li = list(map(int, input().split()))
check = [0] * (2 ** n - 1)
ans = []

for _ in range(n):
    temp = []
    flag = True
    for i, l in enumerate(li):
        if flag and check[i] == 0:
            check[i] = 1
            temp.append(l)
            flag = False
        elif not flag and check[i] == 0:
            flag = True
    ans.append(temp)

for a in ans[::-1]:
    print(*a)

