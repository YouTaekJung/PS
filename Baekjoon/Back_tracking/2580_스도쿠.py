board, blank = [], []
for i in range(9):
    li = list(map(int, input().split()))
    for j, l in enumerate(li):
        if not l:
            blank.append([i, j])
    board.append(li)

def check(x, y):
    s = set()
    for i in range(9):
        for j in range(9):
            if i == x or y == j or (i // 3 == x // 3 and j // 3 == y // 3):
                s.add(board[i][j])
    return list(set(range(1, 10)) - s)

def dfs(count):
    if count == len(blank):
        for b in board:
            print(*b)
        exit()
    x, y = blank[count]
    li = check(x, y)
    for l in li:
        board[x][y] = l
        dfs(count + 1)
        board[x][y] = 0

dfs(0)
