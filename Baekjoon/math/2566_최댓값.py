board = [list(map(int, input().split())) for _ in range(9)]
ans = [0, [0, 0]]
for i in range(9):
    for j in range(9):
        if board[i][j] > ans[0]:
            ans = [board[i][j], [i + 1, j + 1]]
print(ans[0])
print(*ans[1])