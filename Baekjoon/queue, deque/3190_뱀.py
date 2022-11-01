from collections import deque

n, k = int(input()), int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
d, time = 0, 1
snake = deque([[0, 0]])
x, y = 0, 0

l = int(input())
rule = deque([input().split() for _ in range(l)])

while True:
    x, y = x + dx[d], y + dy[d]
    if [x, y] in snake or x in [-1, n] or y in [-1, n]:
        print(time)
        break
    snake.append([x, y])
    if board[x][y]:
        board[x][y] = 0
    else:
        snake.popleft()
    if rule and int(rule[0][0]) == time:
        cur, turn = rule.popleft()
        if turn == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
    time += 1