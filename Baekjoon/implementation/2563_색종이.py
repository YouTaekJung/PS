n = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, min(x + 10, 101)):
        for j in range(y, min(y + 10, 101)):
            board[i][j] = 1

print(sum(list(map(sum, board))))