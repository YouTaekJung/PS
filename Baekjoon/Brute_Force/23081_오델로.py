n = int(input())
mat = []
check = []
ans = [0, [0, 0]]
direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
flag = 0

for i in range(n):
    li = list(input())
    for j in range(n):
        if li[j] == '.':
            check.append([i, j])
    mat.append(li)

for c in check:
    x, y = c
    count = 0
    for d in direction:
        cur = 0
        nx, ny = x, y
        while check:
            nx += d[0]
            ny += d[1]
            if not 0 <= nx < n or not 0 <= ny < n:
                break
            if mat[nx][ny] == 'W':
                cur += 1
            elif mat[nx][ny] == 'B':
                count += cur
                break
            else:
                break
    if ans[0] < count:
        flag = 1
        ans = [count, [y, x]]

if flag == 1:
    print(*ans[1])
    print(ans[0])
else:
    print('PASS')
