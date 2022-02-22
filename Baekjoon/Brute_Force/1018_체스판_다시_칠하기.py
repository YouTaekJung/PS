n, m = map(int, input().split())
res = n * m
board = [input() for _ in range(n)]

for i in range(0, n - 7):
    for j in range(0, m - 7):
        count1 = 0
        count2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2:
                    if board[k][l] == 'W':
                        count1 += 1
                    if board[k][l] == 'B':
                        count2 += 1
                else:
                    if board[k][l] == 'B':
                        count1 += 1
                    if board[k][l] == 'W':
                        count2 += 1
        if min(count1, count2) < res:
            res = min(count1, count2)
print(res)
