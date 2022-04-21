n = int(input())
board = [list(input().split()) for _ in range(n)]
ans = [[0, 0], 0]
pos = 0

def check(i, j):
    count = 0
    for k in range(4):
        while


for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            cur = check(i, j)
            if cur > 1:
                pos = 1
