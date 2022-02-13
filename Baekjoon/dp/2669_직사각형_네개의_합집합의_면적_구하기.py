li = []
x = 0
y = 0
while True:
    try:
        x1, y1, x2, y2 = map(int, input().split())
        li.append([x1, y1, x2, y2])
        if x < x2:
            x = x2
        if y < y2:
            y = y2
    except:
        break

board = [[0] * (y + 1) for _ in range(x + 1)]

for i in range(len(li)):
    for j in range(li[i][0], li[i][2]):
        for k in range(li[i][1], li[i][3]):
            board[j][k] = 1

res = 0
for row in board:
    res += row.count(1)

print(res)