n, m, r = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

process = list(map(int, input().split()))

for p in process:
    n = len(li)
    m = len(li[0])
    if p == 1:
        half = n // 2
        for i in range(half):
            li[i], li[n - i - 1] = li[n - i - 1], li[i]
    elif p == 2:
        for i in range(n):
            li[i] = li[i][::-1]
    elif p == 3:
        res = []
        for i in range(m):
            temp = []
            for j in range(n - 1, -1, -1):
                temp.append(li[j][i])
            res.append(temp)
        li = res
    elif p == 4:
        res = []
        for i in range(m - 1, -1, -1):
            temp = []
            for j in range(n):
                temp.append(li[j][i])
            res.append(temp)
        li = res
    elif p == 5:
        h_row = n // 2
        h_col = m // 2
        res = [li[i][:] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i < h_row and j < h_col:
                    res[i][j] = li[i + h_row][j]
                elif i < h_row and j >= h_col:
                    res[i][j] = li[i][j - h_col]
                elif i >= h_row and j < h_col:
                    res[i][j] = li[i][j + h_col]
                elif i >= h_row and j >= h_col:
                    res[i][j] = li[i - h_row][j]
        li = res
    elif p == 6:
        h_row = n // 2
        h_col = m // 2
        res = [li[i][:] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i < h_row and j < h_col:
                    res[i][j] = li[i][j + h_col]
                elif i < h_row and j >= h_col:
                    res[i][j] = li[i + h_row][j]
                elif i >= h_row and j < h_col:
                    res[i][j] = li[i - h_row][j]
                elif i >= h_row and j >= h_col:
                    res[i][j] = li[i][j - h_col]
        li = res

for l in li:
    print(*l)