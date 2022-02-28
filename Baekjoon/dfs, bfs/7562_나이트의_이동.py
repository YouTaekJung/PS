from collections import deque

n = int(input())
d = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

for _ in range(n):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    queue = deque([start])
    board = [[0] * l for _ in range(l)]
    while queue:
        cur = queue.popleft()
        if cur[0] == end[0] and cur[1] == end[1]:
            break
        for i in range(8):
            x = cur[0] + d[i][0]
            y = cur[1] + d[i][1]
            if 0 <= x < l and 0 <= y < l and board[x][y] == 0:
                board[x][y] = board[cur[0]][cur[1]] + 1
                queue.append([x, y])
    print(board[end[0]][end[1]])