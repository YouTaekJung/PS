n = int(input())
li = list(input().split())
res = [list(range(9, 8 - n, -1)), list(range(n + 1))]
check = ['>', '<']

for i in range(2):
    start = 0
    end = 0
    flag = 1

    for j in range(n):
        if li[j] == check[i]:
            end = j
            if flag == 1:
                res[i][start:end + 1] = res[i][start:end + 1][::-1]
                flag = 0
            start = j + 1
        else:
            if j == n - 1:
                res[i][start:] = res[i][start:][::-1]
            flag = 1
    print(''.join(list(map(str, res[i]))))