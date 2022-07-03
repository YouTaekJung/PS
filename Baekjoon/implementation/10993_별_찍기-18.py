def recur(x, y, m):
    if m == 1:
        star[y][x] = '*'
        return
    r, c = 2 ** (m + 1) - 3, 2 ** m - 1
    if m % 2 == 0:
        for i in range(x, r + x):
            star[y][i] = '*'
        for i in range(1, c):
            star[y + i][x + i] = '*'
            star[y + i][x + r - 1 - i] = '*'

        recur(2 ** (m - 1) + x, y + 1, m - 1)
    else:
        for i in range(x, r + x):
            star[y + c - 1][i] = '*'
        for i in range(c):
            star[y + i][x + int(r / 2) - i] = '*'
            star[y + i][x + int(r / 2) + i] = '*'

        recur(2 ** (m - 1) + x, int(c / 2) + y, m - 1)


n = int(input())
row, col = 2 ** (n + 1) - 3, 2 ** n - 1
star = [[' '] * row for _ in range(col)]

recur(0, 0, n)
for i in range(col):
    r = row - 1 if n % 2 == 0 else row - col + i + 1
    print(''.join(star[i][:r + 1]).rstrip())